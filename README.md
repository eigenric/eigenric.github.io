# Pwaqo

Content and Pelican configurations for my own blog www.pwaqo.tk

I use [Pupil theme](http://github.com/pwaqo/pupil) with
[Summary](https://github.com/getpelican/pelican-plugins/tree/master/summary)
and [Read more link](https://github.com/getpelican/pelican-plugins/tree/master/read_more_link)
plugins.

I've made some changes in the default `Makefile` and `develop_server.sh` scripts
to avoid showing the `pelican.pid` `svr.pid` and to focus on the content (in `blog` folder).


## Ftp Upload

If you want to use this Makefile to upload your work via ftp:

1. Install lftp `sudo apt-get install lftp`
2. Create into `conf` a file called ftp with the next data

```bash
	export FTP_HOST=
	export FTP_USER=a
	export FTP_TARGET_DIR=
	export FTP_PASSWORD=
```
3. Execute

```console
	$ source conf/ftp
	$ make ftp_upload
```

## License


The content of this project itself is licensed under the [Creative Commons Attribution 4.0 license](http://creativecommons.org/licenses/by/4.0/)
and the underlying source code used to format and display that content is licensed under the MIT license (See LICENSE).
