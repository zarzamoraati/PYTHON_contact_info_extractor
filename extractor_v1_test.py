from  extractor_v1 import move_and_clean,match_emails,match_phone_number, concatenate_matches, generate_report, compress_report
import pytest

class TestExtractor:
    def test_match_phones(self):
        message="+1 415.863.9950"
        no_message="+1 4152.863.9950"
        wrong_resp=match_phone_number(message=no_message)
        print(wrong_resp)
        assert len(match_phone_number(message=message)) > 0
        assert len(match_phone_number(message=no_message)) == 0

    def test_match_email(self):
        real_email="john_doe@gmail.com"
        fake_email="johny_blie#fix.py"
        assert len(match_emails(real_email)) > 0
        assert len(match_emails(fake_email)) == 0
    
    def test_concatenate_results(self):
        assert concatenate_matches(emails=[], phones=[]) == ""
        result=concatenate_matches(emails=["someting@gmail.com"],phones=[])
        assert result != ""
        assert isinstance(result,str)
        assert len(result) > 0
                
    def test_generate_report(self):
        """When emails and phones are empty should return false.
        Otherwise return the path"""
        
        assert generate_report(content="") == False
        assert type(generate_report(content="something")) == str
        assert len(generate_report(content="something")) > 0
    
    def test_compress_report(self):
        assert compress_report("pathnoexists") == False

    def test_move_clean(self):
        with pytest.raises(Exception,match=r'any file') as excinfo:
            move_and_clean("not_dir")
        assert excinfo.type is Exception
