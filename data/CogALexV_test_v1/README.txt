
	CogALex-V Shared Task on the Corpus-Based Identification of Semantic Relations
	Organizers: Stefan Evert, Alessandro Lenci, Enrico Santus
	Test Data v1 (2016-09-27)


TASK

See the instructions at: https://sites.google.com/site/cogalex2016/home/shared-task


FILES AND FORMATS

CogALex_Evaluation.py:
  - Official evaluation script, which can be used for both subtasks.
  - To learn how to use it, type: python CogALex_Evaluation.py --help

baselines/:

  baselines/random_task1.txt:
  baselines/random_task2.txt:
    - baseline predictions (random guesses) for the two subtasks
    - also serves as example of the expected system output

  baselines/majority_task1.txt:
  baselines/majority_task2.txt:
    - majority baseline (FALSE for subtask 1, RANDOM for subtask 2)

input.txt:
  - TAB-delimited text file with candidate word pairs (system input)
  - columns: word1, word2

gold_task1.txt:
  - gold standard answers for subtask 1 (related vs. unrelated pairs)
  - TAB-delimited text file with word pairs + Boolean indicating relatedness (expected system output)
  - columns: word1, word2, related? (TRUE, FALSE)

gold_task2.txt:
  - gold standard answers for subtask 2 (relation identification)
  - TAB-delimited text file with word pairs + semantic relation or RANDOM (expected system output)
  - columns: word1, word2, semantic relation (SYN, ANT, HYPER, PART_OF, RANDOM)

relata_metadata.txt:
  - TAB-delimited text files with the following columns (must not be used for training of systems!)
	- relatum: this field contains an uncapitalized lemma or a multiword expression (spaces in multiword expressions are represented with an underscore: e.g. north_carolina).
	- tags: this field contains a comma separated list of tags, with their frequency among the total number of annotators (e.g. "SUPERORDINATE_4/26,PLANT_1/26" stays for "SUPERORDINATE was tagged by 4 subjects out of 26, while PLANT by 1 out of 26"). NOTE: The reliability of the tags is low: we suggest you to rely only on tags that were judged at least twice.
	- frequency: this is an integer representing the frequency of the term in a combination of ukWac and Wackypedia (see the section CORPORA below for more information).
	- term-dominantPOS: this field contains the term with attached the dominant POS (the most frequent one in the abovementioned corpora). The POS tag is attached with an hyphen and it is represented by one of the following letters: j for adjective, n for noun and v for verb.
	- distribution of POS: every POS is provided with the number of occurrences in the abovementioned corpora (POS tagset is available here: http://wacky.sslmit.unibo.it/lib/exe/fetch.php?media=tagsets:ukwac_tagset.txt). POS are slash separated.
	- distribution of forms: we have also collected the inflections and the different capitalizations with their frequencies. Forms are slash separated.
	- distribution of POS and morphological information: a more detailed distribution of POS and morphological information (tagset is available here: http://wacky.sslmit.unibo.it/lib/exe/fetch.php?media=tagsets:ukwac_tagset.txt). Tags are slash separated.

pairs_metadata.txt:
  - TAB-delimited text files with the following columns (must not be used for training of systems!)
  - NB: RANDOM pairs are annotated with "n/a"
	- first relatum: it is one of the relata in the file relata_metadata.txt
	- relation: it can be one of the following relations: Antonym (ANT), Synonym (SYN), Hypernymy (HYPER), Meronymy (PART_OF). For the definition of these relations, please refer to: https://github.com/commonsense/conceptnet5/wiki/Relations.
	- second relatum: it is one of the relata in the file relata_metadata.txt
	- tags: this field contains a comma separated list of tags, with their frequency among the total number of annotators (e.g. "CULTURE_1/5,EVENT_4/5" stays for CULTURE was tagged by 1 subject out of 5, while PLANT by 4 out of 5). NOTE: The reliability of the tags is low: we suggest you to rely on tags that were judged at least twice.
	- sentence: this field contains a sentence that paraphrases the relation; this sentence was used in the crowdsourcing task to assess the quality of the relation.
	- distribution of votes: the next five columns are integers that represent the number of votes for each value, with reference to the sentence in the previous field: "strong disagreement" (the first one, value=1), "disagreement", "neutral", "agreement" and "strong agreement" (the last one, value=5).
	- agreement between subjects as reported by Crowdflower.
	- number of subjects who voted the agreement with the sentence.
	- average agreement of the subjects (in the range between 1="strongly disagree" and 5="strongly agree").
	- variance among the votes.
	- average agreement minus the variance.
	- source from which the pair was extracted.
	- score in the source, if available.


ABOUT THE DATASET

This dataset has been extracted from EVALution 1.0 (Santus et al. 2015), which contains semantic relations and metadata, and was designed for training and evaluation of Distributional Semantic Models (DSMs). EVALution is freely available here: https://github.com/esantus/EVALution/tree/EVALution_v1.0

Frequency information in the EVALution metadata is based on the following corpora:
 - ukWaC: a 2 billion word corpus constructed from the Web limiting the crawl to the .uk domain and using medium-frequency words from the BNC as seeds. The corpus was POS-tagged and lemmatized with the TreeTagger.
 - WaCkypedia_EN: a 2009 dump of the English Wikipedia (about 800 million tokens), in the same format as PukWaC, including POS/lemma information, as well as a full dependency parse (parsing performed with the MaltParser). The texts were extracted from the dump and cleaned using the Wikipedia extractor.

You can find more information about the corpora in the following papers:

 - M. Baroni, S. Bernardini, A. Ferraresi and E. Zanchetta. 2009. The WaCky Wide Web: A Collection of Very Large Linguistically Processed Web-Crawled Corpora. Language Resources and Evaluation 43(3): 209-226 (PDF).
 - M. Baroni and S. Bernardini (eds.). 2006. Wacky! Working papers on the Web as Corpus. Bologna: GEDIT. (Webpage)
 - A. Ferraresi. 2007. Building a very large corpus of English obtained by Web crawling: ukWaC. Master Thesis, University of Bologna (PDF)
 - A. Ferraresi, E. Zanchetta, M. Baroni and S. Bernardini. 2008. Introducing and evaluating ukWaC, a very large web-derived corpus of English. In S. Evert, A. Kilgarriff and S. Sharoff (eds.) Proceedings of the 4th Web as Corpus Workshop (WAC-4) – Can we beat Google?, Marrakech, 1 June 2008. (PDF) (Webpage)


REFERENCES

Enrico Santus, Frances Yung, Alessandro Lenci, and Chu-Ren Huang. 2015. EVALution 1.0: An Evolving Semantic Dataset for Training and Evaluation of Distributional Semantic Models. Proceedings of the 4th Workshop on Linked Data in Linguistics, Beijing.
