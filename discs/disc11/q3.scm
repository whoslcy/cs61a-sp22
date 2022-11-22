(define (reverse lst)
    'YOUR-CODE-HERE
    (define (my_reverse lst_to_reverse result)
        (if (null? lst_to_reverse)
            result
            (my_reverse (cdr lst_to_reverse) (cons (car lst_to_reverse) result))))
    (my_reverse lst nil)
)

(expect (reverse '(1 2 3)) (3 2 1))
(expect (reverse '(0 9 1 2)) (2 1 9 0))
