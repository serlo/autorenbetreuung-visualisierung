CONTACTS := Kontaktsammlung\ Community\ -\ Kontaktdaten.csv
DOT_FILE := visualisierung_autorenbetreuung.dot
PNG_TARGET := visualisierung_autorenbetreuung.png

.PHONY: all
all: $(PNG_TARGET)

$(PNG_TARGET): $(DOT_FILE)
	dot -Tpng $^ > $@

$(DOT_FILE): create_dot_file.py $(CONTACTS)
	python create_dot_file.py $(CONTACTS) $@
