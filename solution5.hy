(import data)

(defmacro printlst [it]
    `(print (list ~it)))

(setv students data.students)
(setv quize data.QUIZE)

(defn cal [quize]
  (fn [student]
    (print student.id
      (reduce
        (fn [x y] (+ x (last (last y))))
        (filter
          (fn [x] (= (first x) (first (last x))))
          (zip student.ans quize))
        0
      )
    )
  )
)

(print "ID\tScore\n==================")

(print (list (map (cal quize) students)))
