(define (cddr s) (cdr (cdr s)))

(define (cadr s) 
    (car (cdr s))
)

(define (caddr s) 
    (car (cdr (cdr s)))
)

(define (ascending? lst) 'YOUR-CODE-HERE
    (if (null? (cdr lst))
        #t
        (if (<= (car lst) (cadr lst))
            (ascending? (cdr lst))
            #f
        )
    )
)

(define (interleave lst1 lst2) 'YOUR-CODE-HERE
    (cond
        ((and (not (null? lst1)) (not (null? lst2)))
            (cons (car lst1) 
                (cons (car lst2) 
                    (interleave (cdr lst1) (cdr lst2)))))
        ((and (not (null? lst1)) (null? lst2))
            lst1)
        ((and (null? lst1) (not (null? lst2))) 
            lst2)
        ((and (null? lst1) (null? lst2))
            nil)))

(define (my-filter func lst) 'YOUR-CODE-HERE
    (if (null? lst)
        lst
        (if (func (car lst))
            (cons (car lst) (my-filter func (cdr lst)))
            (my-filter func (cdr lst)))))

(define (no-repeats lst) 'YOUR-CODE-HERE
    (if (null? lst)
        lst
        (let
            (
                (current_node (car lst))
            )
            (cons 
                current_node 
                (no-repeats (my-filter (lambda (node) (not (= node current_node))) (cdr lst))))
            )
    )
)
