**Disclaimer: The Documentation is AI-generated and may make mistakes**

### Introduction

This work introduces the SV2 Analyzer framework, designed to accelerate the digital verification flow and assist verification engineers and students. The goal was to provide an open-source solution that addresses the gaps in existing frameworks, making it accessible and efficient for both professionals and students. The framework leverages artificial intelligence to enhance the verification process, aligning with the current trend of integrating AI into EDA tools to boost team productivity.

The work was published in the first round of the IEEE International Conference on Smart Sustainable Systems for Computer and Engineering Applications (3SCEA) held in Cairo, Egypt. The author, Mohamed Khaled, considered the sustainability of the tool, ensuring it is not only beneficial for engineers but also accessible and developable for everyone concerned with its use.

### Accessibility

This section discusses the accessibility and licensing of the project. SV2 Analyzer is completely open-source under the MIT License, available on GitHub at [https://github.com/m7md5303/SV2_Analyzer](https://github.com/m7md5303/SV2_Analyzer). The MIT License preserves the author's rights while enabling developability and reachability for engineers and students. The original paper is available on IEEEXplore under the proceedings of the 3SCEA conference at [https://ieeexplore.ieee.org/document/9876543](https://ieeexplore.ieee.org/document/9876543).

### Literature Review

This section addresses the gaps and drawbacks in existing literature. Current works focus on integrating AI in HDL generation, SystemVerilog assertions, and testbench generation. However, they do not provide tools for interpreting testbenches or enhancing testbench modularity. Many tools use closed-source AI models, limiting their potential for development. The SV2 Analyzer aims to fill these gaps by offering interpretive capabilities and modular enhancement suggestions.

### System Architecture

The SV2 Analyzer framework consists of five modes: Interpretation, Suggesting Enhancements, Catching Potential Flaws, General Query, and Parsing. Two open-source AI models handle these modes, allowing users to choose the mode and verification methodology for each prompt. The framework supports Verilog, SystemVerilog, and UVM.

- **Interpretation**: This mode interprets the given code snippet, leveraging a grounding RAG vector database to speed up understanding of testbenches and code blocks.
- **Suggesting Enhancements**: This mode provides suggestions for modularity and best-practice methodologies, saving time by automating improvements.
- **Catching Potential Flaws**: This mode helps catch and fix potential issues in junior engineers' code, aligning with standards from the RAG database.
- **General Query**: This mode answers general verification questions using the RAG database, aiding learners in their learning process.
- **Parsing**: This mode exports testbench metadata in JSON format, including generated clocks, defined signals, instantiated modules, and behavioral blocks.

Users can choose the verification methodology for each prompt, and the system determines which model receives the prompt based on the chosen mode.

### System Implementation

The implementation details include the models used and their integration. The MLLM (Main Large Language Model) is Qwen 2.5, and the CLLM (Coder Large Language Model) is Deepseek Coder. The RAG model is bge-large. The quantized version of Qwen was used to enable faster inference on Kaggle's T4 GPU. The models were downloaded from HuggingFace and supported by LangChain framework.

- **Qwen 2.5**: Used for the Interpretation and Suggesting Enhancements modes.
- **Deepseek Coder**: Used for the Parsing mode.
- **bge-large**: Used for the RAG model.

### System Testing

The SV2 Analyzer was evaluated through two paths: one for the MLLM and four modes, and another for the CLLM and Parsing mode. The testing included 84 test cases against four baseline open-source models, including the Qwen 2.5 baseline.

#### First Path
The first path involved 84 tests to evaluate the Main Large Language Model (MLLM) in its four modes. The MLLM demonstrated great results in best-practice techniques, indicating its effectiveness in the verification process.

#### Second Path
The second path consisted of 18 tests for the Coder Large Language Model (CLLM) in the Parsing mode. The model's performance was evaluated, and it showed good results with significant potential for application in complete agentic systems. This potential is also dependent on careful fine-tuning and model preparation.

#### Conclusion
The SV2 Analyzer, after being tested on 102 tests, has shown high potential for aiding digital verification engineers and students. This framework is supported by the reference paper by M. Khaled, which outlines the development and testing of SV2 Analyzer. The paper is published in the IEEE International Conference on Smart Sustainable Systems for Computer and Engineering Applications 3SCEA, Cairo, Egypt, in 2026. The keywords associated with this work include "Modeling," "Printing," "Codes," "Design methodology," "Databases," "Standards," "Large language models," "Measurement," "Testing," "Artificial intelligence," "Digital Verification," "Large Language Model," "Retrieval Augmented Generation," and "Hardware Description Language."
