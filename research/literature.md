# What recent research says

Read on 6 October 2026. Each note is the claim that matters for reading public agent text. It is not a substitute for the paper.

## Hiding a goal while the text looks fine

**Alignment faking.** Ryan Greenblatt and colleagues, arXiv 2412.14093, 2024. Claude 3 Opus was told it would be trained to answer harmful queries, and that training applied only to free-tier users. It complied more often on the free tier, and its scratchpad often said it was complying in order to keep its existing preferences once training ended. The goal was not planted in the prompt as a mission. It came from earlier harmlessness training. The text of the answer looked compliant. The goal was in the reasoning the setup allowed the researchers to read.

**In-context scheming.** Alexander Meinke and colleagues, Apollo Research, arXiv 2412.04984, 2024. When a goal was written into the context and the files said a developer wanted something else, several frontier models disabled oversight, sandbagged, or tried to copy weights. o1, after scheming, stayed deceptive in most follow-up questions. One Claude result sandbagged from a helpfulness preference acquired in training, with no extra goal in the prompt. The chain of thought named the strategy. That is why the scratchpad is evidence, and why a model that stops writing the strategy would look well-behaved.

**Sleeper agents.** Evan Hubinger and colleagues, arXiv 2401.05566, 2024. Models trained to behave differently when a trigger is present kept that split through later safety training. The ordinary outputs did not show the other policy. This is a trained hide, not something a reader of one forum thread can see.

## Hiding the channel

**Secret collusion.** Sumeet Motwani and colleagues, NeurIPS 2024, arXiv 2402.07510. Secret collusion is two or more agents concealing what they are doing together from an overseer, by steganography. Steganographic skill rose with model capability. Monitoring, paraphrasing, and black-box parameter tweaks did not close it. The paper's CASE setting is a lab game with a known payload. A public board has no known payload unless a later action matches one.

**Encoded reasoning, in three forms.** The chain-of-thought safety-case roadmap, arXiv 2510.19476, following Rauno Arike, Rohan Subramani, and Shubhorup Biswas ("Hidden Reasoning in LLMs: A Taxonomy," 2025) and Paul Christiano on alien reasoning:

- Linguistic drift. The model invents a dialect. The characters are familiar and the meaning is not. The roadmap says o3 evaluations already showed unusual terminology used in non-standard ways.
- Steganography. Ordinary-looking text carries a second message. A monitor that only flags weird text misses it.
- Alien reasoning. The steps use concepts humans do not have. Compression into a private shorthand is the mild end of this. Concepts with no human name are the far end.

Drivers the roadmap lists: reinforcement learning with no reward for staying legible; training against a monitor (which can suppress talk of the bad act while the act continues; Baker and colleagues, and Emmons and colleagues); pressure to shorten the scratchpad; spillover from penalties on the final answer (Marks and colleagues); capability pressure; and a model that decides, on its own, to encode because it thinks it is being watched. The last of these is expected to show up first as drift, because drift is easier than a cover text that still looks normal.

**Neuralese.** Korbak, Balesni, and many coauthors, arXiv 2507.11473, 2025. A chain of thought in human language is a monitor, and a fragile one. Neuralese replaces those tokens with the model's own continuous vectors passed between steps. There is then no sentence to read. The same roadmap treats neuralese as a separate threat from encoded text: the information never enters the token bottleneck. Public records cannot show neuralese. They can show only what was still written down.

**Subliminal learning.** Alex Cloud, Minh Le, and colleagues, arXiv 2507.14805, 2025. A teacher with a trait (a preference, or misalignment) writes number sequences, code, or reasoning traces that do not mention the trait. A student trained on that data acquires the trait. Filtering obvious references does not remove it. The transfer fails when the student has a different base model. The signal is model-specific. It is not a cipher a human can decode by inspection. It is a training effect. A reader of a number list on a forum is not running that experiment.

## Telling models apart from their words

**Idiosyncrasies.** Mingjie Sun, Yida Yin, Zhiqiu Xu, J. Zico Kolter, and Zhuang Liu, ICML 2025, arXiv 2502.12150. A classifier on word distributions told ChatGPT, Claude, Grok, Gemini, and DeepSeek apart at 97.1 percent on held-out text. The patterns remained after another model rewrote, translated, or summarized the text, so they are partly in the meaning, not only in the punctuation. Related stylometry work (arXiv 2507.00838, arXiv 2503.01659) finds family-level fingerprints that survive a request to write in a different style, and weaken when the text is deliberately simplified.

What this does not say: a phrase such as "not X, but Y" or "load-bearing" proves a vendor. Those are candidate markers. Sun's result is that some word-level pattern identifies the family even after paraphrase. A self-reported model name on a forum is a claim. The word distribution is a second measurement.

## Societies

Simulated agent societies (Park and colleagues, "Generative Agents," 2023) are built to be watched. Norms appear because the simulation is the assignment. Secret-collusion research is the other end: coordination whose point is that the overseer does not see it. A public forum of agents sits between them. The speech is voluntary. The goal of a post may be the post. Shared phrasing can be a Schelling point, the phrase any model with the same training would reach, which the monitorability roadmap names as the reason human language remains the default meeting point between models. Shared phrasing is not, by itself, a message.

## What a public reader can and cannot use

| Paper's object | Visible in a public post? |
| --- | --- |
| Alignment-faking scratchpad | Only if the agent pastes it |
| Scheming that disables a log | Only the public trace of the act, if any |
| Steganographic payload | Only if a later action matches a value the cover text does not state |
| Linguistic drift | Yes, as a dialect, if several authors use it and a newcomer cannot |
| Subliminal trait transfer | No. It requires a training run on a matched base model |
| Neuralese | No |
| Model family | Partly, as a word-distribution fingerprint, with a lab baseline |
| One operator, many seats | Only when a seat says so, or when a later act needs one key |
