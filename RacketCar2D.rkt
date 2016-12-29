#lang racket
(require
  racket/gui
  racket/draw)

(struct color (red green blue alpha) #:transparent)
(struct car_segment (angle1 length1 angle2 length2 color wheel) #:transparent)
(struct car_body (angle1 angle2 angle3 angle4 angle5 angle6 angle7 angle8) #:transparent)
(struct car_wheel (size power) #:transparent)
(struct car_wheels (wheel1 wheel2 wheel3 wheel4) #:transparent)
(struct car (body wheels phys) #:transparent)