## Assignment 2

### Characterizing and detecting mismatch in machine-learning systems

The article  [Software Engineering for Machine Learning: Characterizing and Detecting Mismatch in Machine-Learning Systems](https://insights.sei.cmu.edu/blog/software-engineering-for-machine-learning-characterizing-and-detecting-mismatch-in-machine-learning-systems/) by Lewis and Ozkaya (2021) discusses some of the challenges mismatches cause when integrating machine learning components into software systems. Various types of mismatches van occur when there are misaligned assumptions and poor communication between different stakeholders involved in the process.


They identify several categories of mismatches:

**1. Computing-resource mismatches** occur when the necessary computing resources are unavailable in the production environment, leading to poor system performance. 

**2. Data-distribution mismatches** occur when the training data differs significantly from the production data, reducing model accuracy.

**3. API mismatches** occur when there are discrepancies between the expected inputs and outputs of the machine learning component and the system it integrates with, creating glue code.

**4. Test-data mismatches** result from the inability to properly test the machine learning components due to lack of access to appropriate test data or understanding of how to test the model. 

**5. Monitoring mismatch** happen when the production environment's monotiring tools cannot collect relevant machine learning metrics, such as model accuracy.

**6. Task and purpose mismatches** can happen when there are unclear requirements and expectations between project owners and data scientists. This can lead to models that do not meet the business goal. 

**7. Operational environment mismatches** occur when assumptions about the production environment are not communicated, affecting runtime metrics and data collection. 

In summary, they underscore the importance of improved communication and automated detections tools to prevent mismatches. With this they aim to enhance the development and maintenance of machine learning enabled systems. 

I have encountered API mismatches during one of my previous projects, where we were forced to create additional glue code to connect data formats with each other. The output from the preprocessing pipeline was a Seurat object, which contained many components and took an extra step in our pipeline to deconstruct and store in a format our pipeline could handle.

Additionally, during this project, we had to communicate well with everyone involved in the development of the code, as well as those wanting to use it later on, to avoid task and purpose mismatches. Not everyone had the same needs and wants from the project, so we had to make sure to stay in communication every step of the way.

### Tackling collaboration challenges in the development of ml-enabled systems

The article [Tackling Collaboration Challenges in the Development of ML-Enabled Systems](https://insights.sei.cmu.edu/blog/tackling-collaboration-challenges-in-the-development-of-ml-enabled-systems/) by Lewis (2023) discusses the collaboration challenges that arise in the development of machine learning-enabled systems. These systems require both software engineerds and data scientists to work together effectively. To summarise, the main challenges discussed in this article are: aligning the experimental approach of data scientists with the structured principles of software engineering, managing training data, integrating ML models into production systems, and ensuring quality assurance. Here they outline several recommendations to improve these collaborations, such as involving data scientists early in the project, adopting formal documentation practices, and ensuring clear responsibility boundaries. 

In my future collaboration with software engineers, I would aim to be involved early on in the process so that we can align our expectations and goals and distribute our tasks accordingly. A few approaches I could take to structure my code would be to:

1. Work with well-defined functions and classes, which are documented comprehensively.
2. Utilize version control using Git.
3. Include testing frameworks to ensure reliability and maintenance of the code.

During my internship project, I helped develop a pipeline with the aim of making it usable for different project groups. Although there was no collaboration with a software engineer, we still had to be sure to communicate and distribute tasks clearly.

We made sure we created the code in such a manner that was clear and readable as well as structured  in a way that allowed for adaptability. We added different settings so that the code was usable for various purposes. To manage concurrent development, we worked with different branches on GitHub, as I was developing it at the same time as a colleague. 