# -*- coding: utf-8 -*-
#BEGIN_HEADER
from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
from KBaseReportPy.KBaseReportPyClient import KBaseReportPy
import os
from Bio import SeqIO
#END_HEADER


class jayrboltonContigFilter:
    '''
    Module Name:
    jayrboltonContigFilter

    Module Description:
    A KBase module: jayrboltonContigFilter
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/jayrbolton/jayrboltonFilterContig.git"
    GIT_COMMIT_HASH = "2d61c90a22e89d7535ee297d766e25bedd15f299"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.scratch = config['scratch']
        #END_CONSTRUCTOR
        pass

    def filter_contigs(self, ctx, params):
        """
        :param workspace_name: instance of String
        :param params: instance of type "ContigFilterParams" (Input
           parameters) -> structure: parameter "assembly_ref" of String,
           parameter "min_length" of Long
        :returns: instance of type "ContigFilterResults" (Output results) ->
           structure: parameter "report_name" of String, parameter
           "report_ref" of String, parameter "filtered_assembly_ref" of
           String, parameter "n_total" of Long, parameter "n_remaining" of
           Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN filter_contigs
        for name in ['min_length', 'assembly_ref', 'workspace_name']:
            if name not in params:
                raise ValueError('Parameter "' + name + '" is required but missing')
        if not isinstance(params['min_length'], int) or (params['min_length'] < 0):
            raise ValueError('Min length must be a non-negative integer')
        if not isinstance(params['assembly_ref'], basestring) or not len(params['assembly_ref']):
            raise ValueError('Pass in a valid assembly reference string')
        ws_name = params['workspace_name']
        assembly_util = AssemblyUtil(self.callback_url)
        file = assembly_util.get_assembly_as_fasta({'ref': params['assembly_ref']})
        # Parse the downloaded file in FASTA format
        parsed_assembly = SeqIO.parse(file['path'], 'fasta')
        min_length = params['min_length']
        # Keep a list of contigs greater than min_length
        good_contigs = []
        # total contigs regardless of length
        n_total = 0
        # total contigs over the min_length
        n_remaining = 0
        for record in parsed_assembly:
            n_total += 1
            if len(record.seq) >= min_length:
                good_contigs.append(record)
                n_remaining += 1
        # Create a file to hold the filtered data
        filtered_path = os.path.join(self.scratch, 'filtered.fasta')
        SeqIO.write(good_contigs, filtered_path, 'fasta')
        # Upload the filtered data to the workspace
        new_ref = assembly_util.save_assembly_from_fasta({
            'file': {'path': filtered_path},
            'workspace_name': ws_name,
            'assembly_name': file['assembly_name']
        })
        # Create an output summary message for the report
        text_message = "".join([
            'Filtered assembly to ',
            str(n_remaining),
            ' contigs out of ',
            str(n_total)
        ])
        # Data for creating the report, referencing the assembly we uploaded
        html_dir = os.path.join(self.scratch, 'html')
        html_index_path = os.path.join(html_dir, 'index.html')
        file_path = os.path.join(self.scratch, 'myfile.txt')
        with open(file_path, 'w') as f:
            f.write('hello world')
        os.mkdir(html_dir)
        with open(html_index_path, 'w') as f:
            f.write('<p><b>hello world</b></p>')
        html_links = [
            {
                'path': html_dir,
                'name': 'HTML Report Test',
                'description': 'Sample description'
            }
        ]
        file_links = [
            {
                'path': file_path,
                'name': 'Linked file test',
                'description': 'Sample file description'
            }
        ]
        report_data = {
            'objects_created': [
                {'ref': new_ref, 'description': 'Filtered contigs'}
            ],
            'html_links': html_links,
            'file_links': file_links,
            'message': text_message,
            'workspace_name': ws_name
        }
        # Initialize the report
        kbase_report = KBaseReportPy(self.callback_url)
        report = kbase_report.create_extended_report(report_data)
        # Return the report reference and name in our results
        returnVal = {
            'report_ref': report['ref'],
            'report_name': report['name'],
            'n_total': n_total,
            'n_remaining': n_remaining,
            'filtered_assembly_ref': new_ref
        }
        #END filter_contigs

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method filter_contigs return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
