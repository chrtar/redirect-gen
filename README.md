# Redirects generator

Extract the three columns (Source URL, Source URL Status,Destination URL) **without headers** from the excel sheet to a comma separated CSV. It should look like this:

```
http://www.alamo.no/Content/1665/no/EmailProgramme/,301,https://www.alamo.no/
http://www.alamo.no/Content/1665/no/Fleet,301,https://www.alamo.no/biler/us/
http://www.alamo.no/content/1665/no/fleet,301,https://www.alamo.no/biler/us/
http://www.alamo.no/content/1665/no/fleet/main,301,https://www.alamo.no/biler/us/
http://www.alamo.no/Content/1665/no/Fleet/main?selectedCountry=AE,301,https://www.alamo.no/biler/us/
```


Once you have the file generate the config:


```
    python gen.py alamo_fi.csv > alamo_fi.conf

```

