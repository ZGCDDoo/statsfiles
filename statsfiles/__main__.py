from statsfiles import statsfiles
import argparse


parser = argparse.ArgumentParser(
    description='Do the statistics of tabular like files.')
parser.add_argument('iter_start',  type=int,
                    help='iteration start for performing the statistics')

parser.add_argument('--afm', action='store_const', const=True,
                    help='Antiferromagnetism is present')

args = parser.parse_args()

statsfiles.run_statsfiles(args.iter_start, args.afm)
