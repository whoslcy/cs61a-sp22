(define (cadr lst) (car (cdr lst)))

(define (make-kwlist1 keys values)
  (list keys values))

(define (get-keys-kwlist1 kwlist)
  (car kwlist))

(define (get-values-kwlist1 kwlist)
  (cadr kwlist))

(define (make-kwlist2 keys values)
  (if (and (not (null? keys)) (not (null? values)))
    (cons (list (car keys) (car values)) (make-kwlist2 (cdr keys) (cdr values)))
    nil))

(define (get-keys-kwlist2 kwlist)
  (if (null? kwlist)
    nil
    (cons (car (car kwlist)) (get-keys-kwlist2 (cdr kwlist)))))

(define (get-values-kwlist2 kwlist)
  (if (null? kwlist)
    nil
    (cons (cadr (car kwlist)) (get-values-kwlist2 (cdr kwlist)))))

(define (add-to-kwlist kwlist key value)
  (make-kwlist 
    (append (get-keys-kwlist kwlist) (list key)) 
    (append (get-values-kwlist kwlist) (list value))))

(define (get-first-from-kwlist kwlist key)
  (let (
    (keys (get-keys-kwlist kwlist))
    (values (get-values-kwlist kwlist)))
    (cond 
      ((and (null? keys) (null? values)) nil)
      ((equal? key (car keys)) (car values))
      (else (get-first-from-kwlist (make-kwlist (cdr keys) (cdr values)) key)))))

(define (prune-expr expr)
  (define (prune-helper lst)
    (if (null? lst)
      nil
      (if (null? (cdr lst))
        lst
        (append (list (car lst)) (prune-helper (cdr (cdr lst)))))))
  (append (list (car expr)) (prune-helper (cdr expr))))

(define (curry-cook formals body)
  (if (null? (cdr formals))
    (list `lambda formals body)
    (list `lambda (list (car formals)) (curry-cook (cdr formals) body))))

(define (curry-consume curries args)
  (if (null? args)
    curries
    (curry-consume (curries (car args)) (cdr args))))
