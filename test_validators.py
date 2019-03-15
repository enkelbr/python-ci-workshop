import validators


# Invalid URLS
def test_validate_url_nok_malformed_http():
    assert validators.validate_url('http/:/asdf.com/') is False


def test_validate_url_nok_malformed_https():
    assert validators.validate_url('https/:/fdsa.com') is False


def test_validate_url_nok_hostname_only():
    assert validators.validate_url('example') is False


def test_validate_url_nok_s3():
    assert validators.validate_url('s3://my-bucket/') is False


def test_validate_url_nok_missingtld_http():
    assert validators.validate_url('http://missingtld') is False


def test_validate_url_nok_missingtld_https():
    assert validators.validate_url('https://missingtld') is False


def test_validate_url_nok_protocol_only():
    assert validators.validate_url('http://') is False


def test_validate_url_nok_dot():
    assert validators.validate_url('http://.') is False


def test_validate_url_nok_double_dot():
    assert validators.validate_url('http://..') is False


def test_validate_url_nok_dot_trailing_slash():
    assert validators.validate_url('http://../') is False


def test_validate_url_nok_question():
    assert validators.validate_url('http://?') is False


def test_validate_url_nok_double_question():
    assert validators.validate_url('http://??') is False


def test_validate_url_nok_double_question_trailing_slash():
    assert validators.validate_url('http://??/') is False


def test_validate_url_nok_hash():
    assert validators.validate_url('http://#') is False


def test_validate_url_nok_double_hash():
    assert validators.validate_url('http://##') is False


def test_validate_url_nok_space():
    assert validators.validate_url('http://foo.bar?q=Spaces should be encoded') is False


def test_validate_url_nok_double_slash():
    assert validators.validate_url('//') is False


def test_validate_url_nok_double_slash_a():
    assert validators.validate_url('//a') is False


def test_validate_url_nok_triple_slash_a():
    assert validators.validate_url('///a') is False


def test_validate_url_nok_triple_slash():
    assert validators.validate_url('///') is False


def test_validate_url_nok_proto_triple_slash_a():
    assert validators.validate_url('http:///a') is False


def test_validate_url_nok_domain_only():
    assert validators.validate_url('foo.com') is False


def test_validate_url_nok_rdar():
    assert validators.validate_url('rdar://1234') is False


def test_validate_url_nok_h():
    assert validators.validate_url('h://test') is False


def test_validate_url_nok_space_domain():
    assert validators.validate_url('http:// shouldfail.com') is False


def test_validate_url_nok_no_proto():
    assert validators.validate_url(':// should fail') is False


def test_validate_url_nok_space_paren():
    assert validators.validate_url('http://foo.bar/foo(bar)baz quux') is False


def test_validate_url_nok_ftps():
    assert validators.validate_url('ftps://foo.bar/') is False


def test_validate_url_nok_dash_domain():
    assert validators.validate_url('http://-error-.invalid/') is False


def test_validate_url_nok_start_dash():
    assert validators.validate_url('http://-a.b.co') is False


def test_validate_url_nok_end_dash():
    assert validators.validate_url('http://a.b-.co') is False


def test_validate_url_nok_default_route():
    assert validators.validate_url('http://0.0.0.0') is False


def test_validate_url_nok_long_ip():
    assert validators.validate_url('http://1.1.1.1.1') is False


def test_validate_url_nok_short_ip():
    assert validators.validate_url('http://123.123.123') is False


def test_validate_url_nok_number():
    assert validators.validate_url('http://3628126748') is False


def test_validate_url_nok_start_dot():
    assert validators.validate_url('http://.www.foo.bar/') is False


def test_validate_url_nok_start_end_dot():
    assert validators.validate_url('http://.www.foo.bar./') is False


# Valid URLS
def test_validate_url_ok_normal():
    assert validators.validate_url('http://xkcd.com/353') is True


def test_validate_url_ok_trailing_slash():
    assert validators.validate_url('http://xkcd.com/353/') is True


def test_validate_url_ok_parens():
    assert validators.validate_url('http://foo.com/blah_blah_(wikipedia)') is True


def test_validate_url_ok_double_parens():
    assert validators.validate_url('http://foo.com/blah_blah_(wikipedia)_(again)') is True


def test_validate_url_ok_qs():
    assert validators.validate_url('http://www.example.com/wpstyle/?p=364') is True


def test_validate_url_ok_long_qs():
    assert validators.validate_url('https://www.example.com/foo/?bar=baz&inga=42&quux') is True


def test_validate_url_ok_numeric():
    assert validators.validate_url('http://✪df.ws/123') is True


def test_validate_url_ok_authentication():
    assert validators.validate_url('http://userid:password@example.com') is True


def test_validate_url_ok_authentication_trailing_slash():
    assert validators.validate_url('http://userid:password@example.com/') is True


def test_validate_url_ok_authentication_port():
    assert validators.validate_url('http://userid:password@example.com:8080') is True


def test_validate_url_ok_authentication_port_trailing_slash():
    assert validators.validate_url('http://userid:password@example.com:8080/') is True


def test_validate_url_ok_user():
    assert validators.validate_url('http://userid@example.com') is True


def test_validate_url_ok_user_trailing_slash():
    assert validators.validate_url('http://userid@example.com/') is True


def test_validate_url_ok_user_port():
    assert validators.validate_url('http://userid@example.com:8080') is True


def test_validate_url_ok_user_port_trailing_slash():
    assert validators.validate_url('http://userid@example.com:8080/') is True


def test_validate_url_ok_ip():
    assert validators.validate_url('http://142.42.1.1/') is True


def test_validate_url_ok_ip_port():
    assert validators.validate_url('http://142.42.1.1:8080/') is True


def test_validate_url_ok_dash_china():
    assert validators.validate_url('http://➡.ws/䨹') is True


def test_validate_url_ok_unicode():
    assert validators.validate_url('http://⌘.ws') is True


def test_validate_url_ok_unicode_trailing_slash():
    assert validators.validate_url('http://⌘.ws/') is True


def test_validate_url_ok_anchor():
    assert validators.validate_url('http://foo.com/blah_(wikipedia)#cite-1') is True


def test_validate_url_ok_unicode_in_parens():
    assert validators.validate_url('http://foo.com/unicode_(✪)_in_parens') is True


def test_validate_url_ok_something_after_parens():
    assert validators.validate_url('http://foo.com/(something)?after=parens') is True


def test_validate_url_ok_emoji():
    assert validators.validate_url('http://☺.damowmow.com/') is True


def test_validate_url_ok_anchor_qs():
    assert validators.validate_url('http://code.google.com/events/#&product=browser') is True


def test_validate_url_ok_short():
    assert validators.validate_url('http://j.mp') is True


def test_validate_url_ok_encoded():
    assert validators.validate_url('http://foo.bar/?q=Test%20URL-encoded%20stuff') is True


def test_validate_url_ok_arabic():
    assert validators.validate_url('http://مثال.إختبار') is True


def test_validate_url_ok_china():
    assert validators.validate_url('http://例子.测试') is True


def test_validate_url_ok_regex_from_hell():
    assert validators.validate_url('http://-.~_!$&\'()*+,;=:%40:80%2f::::::@example.com') is True


def test_validate_url_ok_leet():
    assert validators.validate_url('http://1337.net') is True


def test_validate_url_ok_dash_domain():
    assert validators.validate_url('http://a.b-c.de') is True


def test_validate_url_ok_https():
    assert validators.validate_url('https://foo_bar.example.com/') is True


def test_validate_url_nok_double_dash_domain():
    assert validators.validate_url('http://a.b--c.de/') is True


def test_validate_url_nok_end_dot():
    assert validators.validate_url('http://www.foo.bar./') is True
