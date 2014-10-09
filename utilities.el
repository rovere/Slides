(defun sanitizeHTML ()
  (interactive)
  (if (use-region-p)
      (progn
       (save-restriction
       	 (narrow-to-region (region-beginning) (region-end))
       	 (goto-char (point-min))
       	 (while (search-forward "<" nil t) (replace-match "&lt;"))
       	 (goto-char (point-min))
       	 (while (search-forward ">" nil t) (replace-match "&gt;"))
	 ) ;; save-restriction
	) ;; progn
    ))

(defun fontify (font-class)
  (interactive "sFont class: ")
  (if (use-region-p)
      (progn
	(save-restriction
	  (narrow-to-region (region-beginning) (region-end))
	  (goto-char (point-min)) (insert (concat "<font class=\"" font-class "\">"))
	  (goto-char (point-max)) (insert "</font>")
	  ) ;; save-restriction
	) ;; progn
    ))

(defun codify (language)
  (interactive "sLanguage: ")
  (if (use-region-p)
      (progn
	(save-restriction
	  (narrow-to-region (region-beginning) (region-end))
	  (sanitizeHTML)
	  (goto-char (point-min)) (insert (concat "<pre data-lang=\"" language "\">\n"))
	  (goto-char (point-max)) (insert "</pre>\n")
	  ) ;; save-restriction
	) ;; progn
    ))


(defun searchLXR()
  "Look up the word under cursor in a LXR as a symbol."
 (interactive)
 (message "Looking for %s" (thing-at-point 'word))
 (browse-url
   ;;(concat "https://cmssdt.cern.ch/SDT/lxr/ident?_i=" (thing-at-point 'symbol))))
   (concat "http://cmslxr.fnal.gov/lxr/ident?_i=" (thing-at-point 'word)))
)
