PREFIX = /usr/local

bibbja: bibbja.sh bibbja.awk bibbja.tsv
	cat bibbja.sh > $@
	echo 'exit 0' >> $@
	echo '#EOF' >> $@
	tar czf - bibbja.awk bibbja.tsv >> $@
	chmod +x $@

test: bibbja.sh
	shellcheck -s sh bibbja.sh

clean:
	rm -f bibbja

install: bibbja
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	cp -f bibbja $(DESTDIR)$(PREFIX)/bin
	chmod 755 $(DESTDIR)$(PREFIX)/bin/bibbja

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/bibbja

.PHONY: test clean install uninstall
