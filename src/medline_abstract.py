from Bio import Medline

# example script to download medline version of the pubmed query
# esearch -db pubmed -query 'antimicrobial resistance' | efilter -mindate 1950 -maxdate 1990 -datetype PDAT | efetch -format medline > 50_90_medline.txt
medline=[]
with open('../data/medline/10_18_medline.txt') as medline_file:
	records = Medline.parse(medline_file)
	for record in records:
		medline.append(record)

for i in range(len(medline)):
	medline_entry = medline[0]
	print(medline_entry)
# 	outpath = 'mesh_10_18/'+ medline_entry.get('PMID')
# 	with open(outpath,'w') as file:
# 		file.write(str(medline_entry.get('MH')))
# 		file.close()

# example script to move expty file
# grep -lrIZ None | xargs -r0 mv -t nonefile/ --
