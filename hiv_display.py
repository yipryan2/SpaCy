#!/usr/bin/env python3

import spacy

abstract = "HIV-1 integrates into the genome of target cells and establishes latency indefinitely. Understanding the molecular mechanism of HIV-1 latency maintenance is needed for therapeutic strategies to combat existing infection. In this study, we found an unexpected role for Apobec3A (apolipoprotein B MRNA editing enzyme catalytic subunit 3A, abbreviated \"A3A\") in maintaining the latency state within HIV-1-infected cells. Overexpression of A3A in latently infected cell lines led to lower reactivation, while knockdown or knockout of A3A led to increased spontaneous and inducible HIV-1 reactivation. A3A maintains HIV-1 latency by associating with proviral DNA at the 5' long terminal repeat region, recruiting KAP1 and HP1, and imposing repressive histone marks. We show that knockdown of A3A in latently infected human primary CD4 T cells enhanced HIV-1 reactivation. Collectively, we provide evidence and a mechanism by which A3A reinforces HIV-1 latency in infected CD4 T cells."

nlp = spacy.load("en_core_web_trf")
doc = nlp(abstract)
docs = [sent.as_doc() for sent in doc.sents]

options = {"fine_grained": True, "compact": True, "collapse_phrases": False}
spacy.displacy.serve(docs, style="dep", options=options)
