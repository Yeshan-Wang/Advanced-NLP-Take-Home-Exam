# extract test case and target argument
def extract_test_case_and_target(sentences):
    test_case = []
    target = []
    for sentence in sentences:
        test_case.append(sentence['test_case'])
        target.append(tuple(sentence['target']))
    test_case_and_target = {"data": test_case, "meta": target}
    return test_case_and_target

# display failures
def format_srl(x, pred, conf, label=None, meta=None):
    try:
        return pred['verbs'][0]['description']
    except IndexError:
        return " ".join(pred['words'])

# extract target argument
def get_arg_span(pred, target_span=[], verb_id=0):
    arg_list=[]
    if len(pred['verbs']) > verb_id:
        predicate_arguments = pred['verbs'][verb_id]
        words = pred['words']
        tags = predicate_arguments['tags']

        for t, w in zip(tags, words):
            arg = t
            if '-' in t:
                arg = t.split('-')[-1]
            if w in target_span:
                arg_list.append(arg)
    return arg_list

# Helper function for the test of Causative Alternation/Long Distance Dependencies/Robustness
def compare_spans(orig_pred, pred, orig_conf, conf, labels=None, meta=None):
    sp_orig = meta[0].split(' ')
    sp_pred = meta[1].split(' ')
    l_orig = set(get_arg_span(orig_pred, sp_orig))
    l_pred = set(get_arg_span(pred, sp_pred))
    if l_orig == l_pred:
        pass_ = True
    else:
        pass_ = False

    return pass_    

# Helper function for the test of Location modifiers
def compare_spans_loc(orig_pred, pred, orig_conf, conf, labels=None, meta=None):
    sp_orig = meta[0].split(' ')
    sp_pred = meta[1].split(' ')
    l_orig = set(get_arg_span(orig_pred, sp_orig))
    l_pred = set(get_arg_span(pred, sp_pred))
    if l_orig == l_pred:
        pass_ = False
    else:
        pass_ = True

    return pass_

# Helper function for the test of voice
def compare_spans_voice(orig_pred, pred, orig_conf, conf, labels=None, meta=None):

    sp_orig = meta[0].split(' ')
    sp_pred = meta[1].split(' ')
    l_orig = set(get_arg_span(orig_pred, sp_orig))
    l_pred = set(get_arg_span(pred, sp_pred, verb_id=1))
    if l_orig == l_pred:
        pass_ = True
    else:
        pass_ = False

    return pass_

# get the target tags from array
def get_tag(test, pair_id, sent_id, verb_id, token_id):
    try:
        return test.results['preds'][pair_id][sent_id]['verbs'][verb_id]['tags'][token_id].replace("I-", "").replace("B-", "")
    except IndexError:
        return ""