CONTACTS := Kontaktsammlung\ Community\ -\ Kontaktdaten.csv
DOT_FILE := visualisierung_autorenbetreuung.dot

.PHONY: all
all: $(DOT_FILE)

$(DOT_FILE): create_dot_file.py $(CONTACTS)
	python create_dot_file.py $(CONTACTS) $@
