from __future__ import division
import csv, sys, json

def gen_header(config_dict):

	num_pr = config_dict['practice_round_len']
	num_rd = config_dict['round_len']

	header = []
	for i in range(num_pr):
		header.append('Practice '+str(i)+' result')
		header.append('Practice '+str(i)+' latency')
	for i in range(num_rd):
		header.append(str(i) + ' result')
		header.append(str(i) + ' latency')

	return header

def gen_row(practice_str, round_str, config_dict):

	num_pr = config_dict['practice_round_len']
	num_rd = config_dict['round_len']

	pr_entries = [None] * num_pr * 2
	rd_entries = [None] * num_rd * 2

	practice_arr = practice_str.split(',')
	for entry in practice_arr:
		vals = entry.split('.')
		if len(vals) < 3:
			break
		pic_idx = int(vals[0])
		action_code = int(vals[1])
		lat = int(vals[2])
		pr_entries[2*pic_idx] = action_code
		pr_entries[2*pic_idx + 1] = lat
	
	round_arr = round_str.split(',')
	for entry in round_arr:
		vals = entry.split('.')
		if len(vals) < 3:
			break
		pic_idx = int(vals[0])
		action_code = int(vals[1])
		lat = int(vals[2])
		rd_entries[2*pic_idx] = action_code
		rd_entries[2*pic_idx + 1] = lat

	return pr_entries + rd_entries
 
def read_and_write_data(infile, outfile, config_dict):

	try:
		inf = open(infile,'rb')
	except:
		print 'error reading file '+infile
		print 'exiting ... '
		sys.exit(1)
	try:
		outf = open(outfile, 'wb')
	except:
		print 'error creating output file '+outfile
		print 'exiting ...'
		sys.exit(1)

	reader = csv.reader(inf)
	writer = csv.writer(outf)

	header_row = reader.next()
	practice_idx = header_row.index(config_dict['practice_round_name'])
	round_idx = header_row.index(config_dict['round_name'])

	header1_row = reader.next()

	writer.writerow(header1_row + gen_header(config_dict))

	for row in reader:
		writer.writerow(row + gen_row(row[practice_idx], row[round_idx], config_dict))

	inf.close()
	outf.close()



def load_config_dict():

	config_dict = {
				'practice_round_name': 'Q1',
				'round_name': 'Q2',
				'practice_round_len': 8,
				'round_len': 20
			}
	if len(sys.argv) >= 4:

		conf_file = sys.argv[3]
		try:
			with open(conf_file) as f:
				file_dict = json.load(f)
				config_dict.update(file_dict)
		except:
			print 'error loading config file '+conf_file
			print 'exiting ...'
			sys.exit(1)
	return config_dict

if __name__ == '__main__':

	if len(sys.argv) <3:
		print 'Usage: python pod_parser.py <infile_name> <outfile_name> (optional) <config_file>'
		sys.exit(1)
	infile = sys.argv[1]
	outfile = sys.argv[2]
	config_dict = load_config_dict()

	read_and_write_data(infile, outfile, config_dict)