(define (map-fn fn lst)
    (if (not (null? lst))
        (cons (fn (car lst)) (map-fn fn (cdr lst)))
        nil
    )
)


(expect (map-fn (lambda (x) (* x x)) '(1 2 3)) (1 4 9))