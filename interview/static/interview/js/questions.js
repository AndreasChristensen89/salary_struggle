// if there is an answer, the correct answer is written as the following:
// a = intellect
// b = charm
// c = coding
// d = wild
// This is due to the questions with no answers being evaluated according to stats...
// ... and buttons therefore have these values encoded

const hrQuestions = [
    {
      question: "What's your greatest weakness?",
      a: "If I am not challenged I tend to drift towards other tasks.",
      b: "My coding is still not on an advanced level.",
      c: "I'm a bit of a lone wolf. I prefer to work alone.",
      d: "Don't have any.",
      answer: "",
    },
    {
      question: "What's your greatest strength?",
      a: "My analytical skills and my problem solving.",
      b: "My motivation, attitude, and my way with words.",
      c: "I could code my way out of a bar fight.",
      d: "I am a mountain of strength.",
      answer: "",
    },
    {
      question: "Why should we hire you?",
      a: "To become a smarter and better organized company.",
      b: "With my personality I will make your workplace happier.",
      c: "I can code anything for you.",
      d: "Because you'll be doomed if you don't.",
      answer: "",
    },
    {
      question: "Tell me about your motivation for this role.",
      a: "I want to be challenged in an intellectual position.",
      b: "I love to make people work better together.",
      c: "I want to bring your coding quality to the next level.",
      d: "Well, money. I'll do anything for money.",
      answer: "",
    },
    {
      question: "What's the name of our company?",
      a: "A.S Herman Spectrum",
      b: "Cisco Media",
      c: "Data Drifters",
      d: "Never mind the name, I'll succeed anywhere.",
      answer: "coding",
    },
    {
      question: "Do you know what we do here?",
      a: "Streaming service.",
      b: "Accounting software.",
      c: "Database integrations.",
      d: "Hire people like me to win.",
      answer: "coding",
    },
  ];

  const codingQuestions = [
    {
      question: "What's the key difference between lists and tuples?",
      a: "Lists cannot be altered while tuples can",
      b: "Lists can hold integers",
      c: "Lists are mutable while tuples are immutable",
      answer: "c",
      charm: "Look the interviewer deep in the eyes and let the charm take effect",
      intellect: "Argue that that there are more urgent matters at hand",
      coding: "Cite all built-in data types in Python along with their uses",
    },
    {
      question: "What does global scope mean in Python?",
      a: "It's the objects in the current function",
      b: "Refers to the objects available throughout the code execution",
      c: "Refers to all global 'var' variables that are accessible across functions",
      answer: "b",
      charm: "Explain that we should instead talk about how great the interviewer looks",
      intellect: "Argue that trivial details like these will be dealt with later",
      coding: "Demonstrate perfect understanding of scope in Python",
    },
    {
      question: "What is the use of self in Python?",
      a: "It refers to the instance of the class",
      b: "It refers to the class",
      c: "It's the keyword of any given class",
      answer: "a",
      charm: "Explain that scopes are great, but what's really important is the interviewer's role",
      intellect: "Argue that trivial details like these will be dealt with later",
      coding: "Perfectly demonstrate proper scope usage in Python and JavaScript",
    },
    {
      question: "What is Python's __init__?",
      a: "An optional method in classes to create variables",
      b: "A call to prevent the default of an onclick event",
      c: "A contructor method which is automatically called when a new object/instance is created",
      answer: "c",
      charm: "Explain that scopes are great, but what's really important is the interviewer's role",
      intellect: "Argue that trivial details like these will be dealt with later",
      coding: "Perfectly demonstrate proper scope usage in Python and JavaScript",
    },
    {
      question: "Which of the following programming language is the worst?",
      a: "Java",
      b: "C",
      c: "Kobolt",
      answer: "b",
      charm: "Compliment his choice of clothing",
      intellect: "Argue that context is always to be considered",
      coding: "Write an impressive function in each language",
    },
    {
      question: "Given two integers ('a' and 'b'), write a correct pythonic return statement for multiplying them?",
      a: "return a * b",
      b: "return a * b;",
      c: "return @a * b",
      answer: "a",
      charm: "Tell him know that it would be an honor to work with him",
      intellect: "Let him know that the company has bigger isuues that returning integers",
      coding: "Blindfold yourself and write the function",
    },
  ];

  const hardCodingQuestions = [
    {
      question: "Do you think we'll actually be better off with you in our team?",
      a: "I'll take you to the stars.",
      b: "It's the inevitable outcome. I've done the math.",
      c: "I've seen your code. I can do better.",
    },
    {
      question: "You think you're better than me?",
      a: "Only if you let me.",
      b: '"Better" is subjective and irrelevant to this interview',
      c: "My coding has rarely been outmatched.",
    },
    {
      question: "You last chance to give me something good to end this interview with.",
      a: "Go with me and I'll make your dreams come true.",
      b: "No need. I've already deduced that you need me.",
      c: "My skills speak for themselves, Q.E.D.",
    },
  ];