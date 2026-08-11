# SV2 Analyzer
## Introduction

This work introduces the SV2 Analyzer framework for accelerating the digital verification flow and helping verification engineers with their duties. The goal was to provide an open-source solution that is available for both engineers and students. The intend was to provide what is lacking in other frameworks in the literature in the most possible efficient way.
Framework has name SV2 Analyzer
Framework targets accelerating digital verification flow
Framework targets helping verification engineers and students
Framework proposes open-source solution
Framework has purpose or intent providing solution for what is lacking from frameworks in literature
The work is built in an era where almost all of Electronic Design Automation companies are keen on embedding Artificial Intelligence solutions to their tools for increasing the productivity of working teams.
Current era associated with embedding AI in used tools
EDA stands for Electronic Design Automation
EDA supplies their tools with AI solutions
Integrating AI with EDA tools leads to increasing teams productivity
The work author has considered the sustainability of such a tool so that the result is not just helping engineers with their duties but also to produce a developable memory-efficient and reacahble tool for everyone who might be concerned about using the tool.
The work author is Mohamed Khaled and he published the work in the first round of the IEEE International Conference on Smart Sustainable Systems for Computer and Engineering Applications held in Cairo, Egypt
Work author consider sustainability of the tool
Work author is called Mohamed Khaled
Work author is the publisher of the work in  IEEE International Conference on Smart Sustainable Systems for Computer and Engineering Applications
IEEE International Conference on Smart Sustainable Systems for Computer and Engineering Applications has abbreviation 3SCEA
IEEE International Conference on Smart Sustainable Systems for Computer and Engineering Applications takes place at location Cairo in Egypt
The tool has prerequisite memory-efficiency
The tool has prerequisite reachability
## Accessibility

This section discusses the accessibility and the license associated with the project
SV2 Analyzer is completely open-source under the MIT License. The code is published on GitHub at the repository https:
SV2 Analyzer associated with MIT License
SV2 Analyzer has resource/reference https:
MIT License is a well-known license for open-source projects while preserving the author rights
MIT License is known for licensing open-source projects
MIT License results in preserving the author rights
The code was deliberately provided as open-source to allow for developability and reachability for engineers and students
Publishing the code enables developability
Publishing the code enables reachability by engineers and students
The original paper is available on IEEEXplore under the proceedings of the 3SCEA conference. The paper link is https:
Original paper was published by IEEEXplore
Original paper is a part of 3SCEA proceedings
Original paper has resource/reference https:
## Literature Review

This section tackles some of the lacks and drawbacks that present in works in the literature that caused the author to consider them in his work
Works in literature focused on integrating AI in the chip design flow through the automatic generation of HDL codes. Another approach was to integrate AI to the verification flow through generation of SystemVerilog assertions, autoamtic generation of testbenches or using it in a feedback loop for achieving the maximum coverage.
The author noticed no tools are concerned with helping verification engineers to interpret their colleagues testbenches or tools that contribute to enhancing the modularity and the structure of the testbench itself. Additionally, many tools were utilizing closed-source AI models affecting the potential of developability.
Works in literature consider HDL generation automation
Works in literature consider SystemVerilog assertions generations
Works in literature consider introducing testcases for increasing coverage results
Works in literature does not contain features of interpreting testbenches
Works in literature does not contain features for suggesting enhancements for the testbench modularity and quality
Works in literature contains mostly closed-source AI models
Closed-source AI models affects badly the potential of developing tools using them
## System Architecture

This section is dedicated for explaining the system architecture and how the SV2 Analyzer works
SV2 Analyzer has 5 modes. They are Interpretation, Suggesting Enhancements, Catching Potential Flaws, General Query and Parsing. 2 open-source AI models are responsible for these 5 modes while allowing the user to choose which mode he would like to user for each sent prompt. The user is also free to choose which verification methodology is related to his prompt. As the framework supports Verilog, SystemVerilog and UVM
SV2 Analyzer contains 5 modes
SV2 Analyzer supports Verilog
SV2 Analyzer supports SystemVerilog
SV2 Analyzer supports UVM
SV2 Analyzer consists of 2 open-source AI Models
SV2 Analyzer Modes contains Interpretation
SV2 Analyzer Modes contains Suggesting Enhancements
SV2 Analyzer Modes contains Catching Potential Flaws
SV2 Analyzer Modes contains General Query
SV2 Analyzer Modes contains Parsing
SV2 Analyzer user determines the used verification methodology for each prompt
The Interpretation mode is responsible for interpreting the given code snippet according to the knowledge the model has already besides the grounding RAG vector database. It speeds up the understanding of testbenches and the used codeblocks.
Interpretation mode used for interpreting the given code snippet
Interpretation mode used for speeding up the udnerstanding of testbenches and the used code blocks in it
RAG stands for Retrieval Augmented Generation as it counts on getting the important data relevant to the users query from the constructed database by the system designer. The first four modes of the tool use the RAG technology for making the best out of the resources and grounding the answer as much as possible
RAG stands for Retrieval Augmented Generation
RAG used for supporting the LLM with grounding data from a vector database
The first four modes has feature RAG
The second mode is Suggesting Enhancements which proposes to the user how he can modualrize his tetbench and also how to make it disciplined witht he best-practice methodologies in verification. This should save more time than the counting on asking senior engineers or other teams.

Suggesting Enhancements mode proposes enhancements to the user
Suggesting Enhancements mode targets saving more time for improving the testbench
Suggested enhancements includes how to modularize the testbench
Suggested enhancements includes how to make the testbench aligned with best-practice techniques
The third mode is Catching Potential Flaws, as mostly, especially among junior engineers and students, their codes are vulenrable to either logical or syntactical errors. This mode should help them to catch early these flaws and how to fix them according to the standards provided tot he model in the RAG database.
Catching Potential Flaws mode supports junior engineers and students in catching potential issues with their codes
Catching Potential Flaws mode is supported by RAG database
The fourth mode is General Query. This is responsible for answering general questions related to digital verification with the help of the RAG database. It should help learners to accelerate their learning process without the heavy need to watch long videos or explore large documents.
General Query mode enables having a talking database for verification supports students and learners for speeding up their learning process.
These four modes are under the responsibility of one of the two models. It is called the Main Large Language Model and abbreviated as MLLM.
Main Large Language Model is the base of operations for four modes
Main Large Language Model has abbreviation MLLM
Meanwhile, the fifth mode is called Parsing and it is responsible for exporting the metadata of the testbench in JSON format. This data is the generated clocks, defined signals, instantiated modules and the behavioral blocks defined. This mode is under the responsibility of the second AI model and is called the Coder Large Language Model and abbreviated as CLLM. It is called like that because a Coder model was used since it is more suitable for such a task as its input is HDL and its output is JSON
Coder Large Language Model has abbreviation CLLM
Coder Large Language Model enables parsing the testbench metadata
Testbench metadata contains generated clocks
Testbench metadata contains defined behavioral blocks
Testbench metadata contains instantiated modules
Testbench metadata contains defined signals
## System Implementation

This document section talks about some of the details of the framework implementation
The used MLLM was QWEN 2.5 while the CLLM was Deepseek Coder. The RAG model is bge-large. The reason for choosing these models was due to their being open-source models and have suitable sizes. The quantized version of Qwen was used to enable faster inference where the host GPU was Kaggle cloud T4. The three models were downloaded from HuggingFace. The two models were supported by well-designed system prompts while making use of LangChain framework
SV2 Analyzer contains Qwen 2.5
SV2 Analyzer contains Deepseek coder
RAG model is called bge-large
Quantization for QWEN 2.5 enables faster inference
Quantization for QWEN 2.5 enables less memory
Author makes use of Kaggle GPU T4 for hosting the system
The two models is supported by system prompt
The two models makes use of Langchain Framework
The two models has resource/reference HuggingFace
The user enters his prompt associated with the desired mode along with the target verification methodology.
Using the framework implies choosing the desired mode
Using the framework implies choosing the target verification methodology
Inside the pipeline, the system determines whether the MLLM or the CLLM would receive the incoming prompt according to the chosen mode.
Code logic determines which LLM to receive the prompt
The chosen mode is the base of the operating LLM for each mode
## System Testing

This part of the documentation discusses how the SV2 Analyzer was evaluated
The system testing was divided into two paths where one of them was concerned about the MLLM and the four modes underneath while the second path was for evaluating the CLLM and the Parsing mdoe underneath
system testing includes two paths
The first path had 84 test cases against four baseline open-source models including the baseline Qwen 2.5 itself. The framework represented in the MLLM has shown great results while being concerned about the best-practice techniques
The second path had 18 tests to check its effictiveness. The model showed good results with very high potential to be employed in complete agentic systems after careful finetuning and model preparation
first path contains 84 tests for the MLLM in its four modes
second path contains 18 tests for the CLLM in the Parsing mode
system testing results in showing high potential for the framework for helping digital verification engineers and students
## Conclusion

SV2 Analyzer has shown high potential for helping digital verification engineers and students after being tested on 102 tests.
SV2 Analyzer has resource/reference M. Khaled, "SV2 Analyzer: Open-Source Large Language Model-Based Framework for Accelerating Digital Circuits Verification Flow," 2026 IEEE International Conference on Smart Sustainable Systems for Computer and Engineering Applications 3SCEA, Cairo, Egypt, 2026, pp. 374-379, doi: 10.1109/3SCEA68071.2026.11602718. keywords: {Modeling;Printing;Codes;Design methodology;Databases;Standards;Large language models;Measurement;Testing;Artificial intelligence;Digital Verification;Large Language Model;Retrieval Augmented Generation;Hardware Description Language},
