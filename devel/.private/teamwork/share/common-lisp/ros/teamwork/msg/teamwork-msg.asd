
(cl:in-package :asdf)

(defsystem "teamwork-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "KeyData" :depends-on ("_package_KeyData"))
    (:file "_package_KeyData" :depends-on ("_package"))
  ))