(define (list-concat a b)
    'YOUR-CODE-HERE
    (if (null? (cdr a))
        (cons (car a) b)
        (cons (car a) (list-concat (cdr a) b))
    )
)

(expect (list-concat '(1 2 3) '(2 3 4)) (1 2 3 2 3 4))
(expect (list-concat '(3) '(2 1 0)) (3 2 1 0))
