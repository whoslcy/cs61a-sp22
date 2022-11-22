(define (sum lst)
    'YOUR-CODE-HERE
    (define (my_sum lst sum_for_now)
        (if (null? lst)
            sum_for_now
            (my_sum (cdr lst) (+ sum_for_now  (car lst)))))
    (my_sum (cdr lst) (car lst)))

(expect (sum '(1 2 3)) 6)
(expect (sum '(10 -3 4)) 11)
