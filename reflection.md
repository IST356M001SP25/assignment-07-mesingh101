# Reflection

Student Name:  Mera Singh
Sudent Email:  mesingh@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`
This assignment really helped me get more comfortable using Playwright to scrape dynamic websites. I learned how to find elements using CSS selectors, move around the page structure with nextElementSibling, and extract data from each menu section in a way that felt organized. It was cool seeing how everything came together into a clean CSV file.

One thing that tripped me up at first was figuring out how to go from a menu title down to the right <div> that actually held the menu items. The DOM structure wasn’t super clear at first, so I had to play around with the element relationships and try different approaches until it worked. I also ran into a couple of annoying Python import errors—mainly because I didn’t fully get how imports behave when you’re running files from different folders. Once I understood that from code.menuitem wasn’t going to work inside the code/ folder, things clicked.

Another challenge was making sure the selectors I used actually matched what was on the page—especially since the menu layout had lots of nested divs. It helped to use DevTools and really look at the structure before writing the code. I also got a better feel for using dataclasses in Python, and how they make it super easy to organize scraped data.

If anything, I think I still need more practice navigating complex page structures and making sure I’m grabbing the right elements efficiently. But overall, I feel way more confident in using Playwright for web scraping now, and I know I could apply this same process to another restaurant menu or similar page.
