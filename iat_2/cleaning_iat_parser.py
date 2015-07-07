from __future__ import division
import sys, csv

PRIMES = ['water', 'pencil']
CATEGORIES = ['actual','nonsense']
TARGET_TYPES = ['washing','drinking','water-irrelevant','control']
TARGET_WORDS = [
					[
						'clean','wash','scrub','soap','shower','rinse',
						'cup','bottle','drink','glass','mug','liquid',
						'irrigate','ocean','swim','rain','river','flood',
						'speaker','town','paper','sheet','radio','music'
					],
					[
						'sast','imm','citia','snard','terhed','dagon',
						'adhem','dangla','andis','strobi','poseb','joul',
						'halco','sopha','pone','metens','distat','climp',
						'fective','tardue','oduca','biana','maleon','preits'
					]
				]
N_PRACTICE = 4
TARGETS_PER_TYPE = 6

def parse_file(infilename, outfilename):

	with open(infilename,'rU') as infile:
		with open(outfilename, 'w') as outfile:

			reader = csv.reader(infile)
			writer = csv.writer(outfile)

			header1 = reader.next()
			header2 = reader.next()
			result_idx = header1.index('Q78')
			response_id = 0

			header_out = ['ID','TARGETID','CATEGORY','CORRECT','RT (ms)','PRIMETYPE','TARGETTYPE','TARGETWORD']
			writer.writerow(header_out)

			for row in reader:
				responses = row[result_idx].split(',')
				#print len(responses)
				if len(responses) != 101: # wtf
					continue
				iat_response = [[int(x) for x in resp.split('.')] 
						for resp in responses[N_PRACTICE:-1]]

				for resp in iat_response:
					targetid, cat, prime, selected, rt = resp
					category = CATEGORIES[cat]
					if cat == selected:
						correct = 'C'
					else:
						correct = 'X'
					primetype = PRIMES[prime]
					if cat == 1:
						targettype = 'nonsense'
					else:
						targettype = TARGET_TYPES[targetid // TARGETS_PER_TYPE]
					targetword = TARGET_WORDS[cat][targetid]

					outdata = [row[response_id],targetid,category,correct,rt,primetype,targettype, targetword]
					#print outdata
					writer.writerow(outdata)






if __name__ == '__main__':
	infilename = sys.argv[1]
	outfilename = sys.argv[2]
	parse_file(infilename, outfilename)