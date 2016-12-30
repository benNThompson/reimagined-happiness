#lang racket
(require
  racket/gui
  racket/draw)

(struct color (red green blue alpha) #:transparent)
(struct car_wheel (size power color) #:transparent)
(struct car_segment (angle1 length1 angle2 length2 color wheel) #:transparent)
(struct car_body (segment1 segment2 segment3 segment4) #:transparent)
(struct phys_info () #:transparent)
(struct car (body wheels phys) #:transparent)
