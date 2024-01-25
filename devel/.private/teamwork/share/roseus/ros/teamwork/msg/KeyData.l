;; Auto-generated. Do not edit!


(when (boundp 'teamwork::KeyData)
  (if (not (find-package "TEAMWORK"))
    (make-package "TEAMWORK"))
  (shadow 'KeyData (find-package "TEAMWORK")))
(unless (find-package "TEAMWORK::KEYDATA")
  (make-package "TEAMWORK::KEYDATA"))

(in-package "ROS")
;;//! \htmlinclude KeyData.msg.html


(defclass teamwork::KeyData
  :super ros::object
  :slots (_router_key _display_key ))

(defmethod teamwork::KeyData
  (:init
   (&key
    ((:router_key __router_key) "")
    ((:display_key __display_key) "")
    )
   (send-super :init)
   (setq _router_key (string __router_key))
   (setq _display_key (string __display_key))
   self)
  (:router_key
   (&optional __router_key)
   (if __router_key (setq _router_key __router_key)) _router_key)
  (:display_key
   (&optional __display_key)
   (if __display_key (setq _display_key __display_key)) _display_key)
  (:serialization-length
   ()
   (+
    ;; string _router_key
    4 (length _router_key)
    ;; string _display_key
    4 (length _display_key)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _router_key
       (write-long (length _router_key) s) (princ _router_key s)
     ;; string _display_key
       (write-long (length _display_key) s) (princ _display_key s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _router_key
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _router_key (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _display_key
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _display_key (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get teamwork::KeyData :md5sum-) "479cab83ef8c9b1034cf5fc201002f01")
(setf (get teamwork::KeyData :datatype-) "teamwork/KeyData")
(setf (get teamwork::KeyData :definition-)
      "# KeyData.msg
string router_key
string display_key


")



(provide :teamwork/KeyData "479cab83ef8c9b1034cf5fc201002f01")


