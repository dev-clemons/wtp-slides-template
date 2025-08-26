<div style="height: 90pt;"></div>
<div style="flex: 0 0 8%; margin-top: -10pt;">
<img src="https://upload.wikimedia.org/wikipedia/commons/9/99/ETH_Z%C3%BCrich_Logo_black.svg"/>
</div>
<div style="flex: 0 0 65%; text-align: center;">
<h1 style="margin-bottom: 10pt;">Automatic Assessment for Visual Computing in browser based programming</h2>
</div>
<div style="flex: 1">
    <div style="display: flex; align-items: center;">
        <img style="height: 20pt; width: 20pt; margin: 5pt;" src="icons/fontawesome/brands/github.svg">
        <div style="font-size: 0.9rem; margin-right: 5pt;"><a href="https://github.com/dev-clemon">https://github.com/dev-clemon</a></div>
    </div>
    <!-- <div style="display: flex; align-items: center;">
        <img style="height: 20pt; width: 20pt; margin: 5pt;" src="icons/fontawesome/brands/twitter.svg">
        <div style="font-size: 0.9rem;"><a href="https://twitter.com/PatrickKidger">@PatrickKidger</a></div>
    </div> -->
</div>

--split--

# 1. Introduction

Visual programming are often used in introductory programming courses due to giving direct feedback to the user. However they do come with some drawbacks. One of them is autograding them. Opposed to working with text output, visual output is sometimes harder to evaluate. While professional testing tools use screenshot comparison, this might not be the correct way in computer science education. In the last few years, we have developed WebTigerPython a web-based IDE often used in schools in the german speaking area, and are planning to integrate automated testing for the platform

# 2. WebTigerPython

WebTigerPython browser based is a Python IDE used in computer science educations

- Zero-Installation: Runs directly in any modern web browser.
- Universal Access: Works on any device (laptops, tablets, Chromebooks).
- Powerful Libraries: Built-in support for Turtle Graphics, micro:bit, and much more.
- Beginner-Friendly: Features an interactive debugger and simplified syntax to lower the barrier to entry.
- High Ceiling: Advanced Libraries like Pygame, numpy or scipy are also supported

# Automated Assessment

Creating and grading programming assignments, especially visual ones, is time-consuming for educators.

- Traditional unit tests are insufficient for visual output.
- Defining test cases requires deep knowledge and limits code structure.

Heatmaps can be useful but might be overwhelming for novice users. Additionally they require a pixel perfect solution
<img src="./squares-diff.png"/>

--split--

# Our Approach: Multi-Modal Automatic Assessment

One of the main reasons our IDE is popular is according to teacher feedback is that

We move beyond standard unit testing by analyzing multiple facets of a student's submission to provide a holistic assessment.



- Scalable Assessment: Enable large-scale courses to use visual assignments with automated, consistent grading.

- Rich Feedback: Provide students with immediate feedback on both visual correctness and code quality.

- Learning Analytics: Gain insights into common student errors and misconceptions in visual programming domains.

- Reduced Cognitive Load: Develop assessment methods that do not force specific code structures, allowing students to focus on problem-solving.


# 4. Future Work