PY=python
PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/blog
OUTPUTDIR=$(BASEDIR)/conf/output
CONFFILE=$(BASEDIR)/conf/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/conf/publishconf.py
SERVER_SCRIPT=$(BASEDIR)/conf/develop_server.sh

DEFAULT_EDITOR = 'subl'

# Datos ftp

FTP_HOST=ftp.youngeek.tk
FTP_USER=u944951978
FTP_TARGET_DIR=/public_html


help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make ver                         (re)generate and serve site        '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make devserver                   start/restart develop_server.sh    '
	@echo '   make stopserver                  stop local server                  '
	@echo '   make rsync_upload                upload the web site via rsync+ssh  '
	@echo '   make ftp                         upload the web site via FTP        '
	@echo '   make s3_upload                   upload the web site via S3         '
	@echo '   make github                      upload the web site via gh-pages   '
	@echo '   make edit                        for edit the site                  '
	@echo '   make conf                        for config my site                 '


html: clean $(OUTPUTDIR)/index.html

$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

regenerate: clean
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

ftp: publish
	lftp ftp://$(FTP_USER)@$(FTP_HOST) -e "mirror -R $(OUTPUTDIR) $(FTP_TARGET_DIR) ; quit"

ver: html
	cd $(OUTPUTDIR) && $(PY) -m pelican.server
	google-chrome http://localhost:8000

devserver:
	$(SERVER_SCRIPT) restart

stopserver:
	kill -9 `cat pelican.pid`
	kill -9 `cat srv.pid`
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'


rsync_upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvz --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

s3_upload: publish
	s3cmd sync $(OUTPUTDIR)/ s3://$(S3_BUCKET) --acl-public --delete-removed

github: publish
	ghp-import $(OUTPUTDIR)
	git push origin gh-pages

edit: 
	$(DEFAULT_EDITOR) $(INPUTDIR)

conf:
	$(DEFAULT_EDITOR) $(CONFFILE)

.PHONY: html help clean regenerate serve devserver publish ssh_upload rsync_upload dropbox_upload ftp_upload s3_upload github conf edit