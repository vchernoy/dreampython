# QA ⏤ Quality Assurance

## QA Part 1: Intro

Quality Assurance exists in almost any industry, otherwise a product in normal condition would not leave the production process.

Let's talk primarily about Software QA, that is, ensuring the quality of the software being developed, that is, the quality of programs.

The most obvious area of Software QA is checking the program's interface, which can be WEB, mobile app, or other types of interaction between a person and a program.

Roughly speaking, a person sees buttons, windows, input fields in front of them, and must click something with the mouse so that the program reacts somehow.

QA must ensure correct program execution for any user actions. That is, for correct behavior, the program should give the right response, and nothing extra should happen. And for incorrect client behavior, the program should not crash and should respond adequately (with a message on the screen, a hint, etc.). Of course, also not doing anything extra, everything should be within some specification or description.

Testers, QA testers are exactly engaged in checking programs for adequate behavior. Usually testers create (or use an existing) group of tests and run all tests on the next version of the program.

Testing is part of the software development work cycle!

For example, developers release a new version (once a month/week/day), and testers run tests, if they find defects (bugs), they pass all information to programmers for fixing. And then in circles!

---

## QA Part 2: Manual vs. Automation

Manual testing (Manual QA): the tester simulates client behavior, clicks the mouse, enters data, checks the program's behavior against expectations and runs all tests one by one.

Manual testing is usually very labor-intensive, you have to repeatedly repeat the same tests. Eventually it becomes profitable to automate the testing process (Automated QA). This can happen earlier if automation is relatively easy to write and the product specification is well written. More often automation is slowed down by constant changes in the product description, and then test automation can be pushed closer to official product releases.

Automation is written in some programming language (Java, Python), using platforms and infrastructure suitable for testing this product. Automation represents a group of programs, each of which runs a separate test simulating certain user behavior. Writing such a test is usually more difficult than testing manually, but then repeated runs of the finished test are significantly cheaper than manual testing.

Test automation pays off far from immediately, because
* first, writing tests takes time, and
* second, the product specification can change significantly, which may require constant changes and adaptation of tests, because tests can fail not because the program has a defect, but because the test is outdated and does not match the specification.

So it turns out that manual testing comes first — it's easier to start, and then automation begins to be developed, which can pay off in the long run!

---

## QA Part 3: Testing the Product

For example, let's take... a refrigerator, what difference does it make?! Yes, most products are probably purely software (that is, we created a program and test it), but there are many with hardware (that is, with some construction, chips, in a box, mobile phones, for example).

In a refrigerator, for example, there are buttons, a door, sensors, chips, as well as a program that controls temperature or various modes. The refrigerator consists of different parts, with its own design and control. All of this can be tested separately and together.

* Both software and physical parts are subject to testing. Automation is easier to write for the program, and you can make it so that signals about button presses go to the program from the test, not from a real press. So automation will help a lot in this part.

* As for physical manipulations, for example, pressing buttons (ice, water) and simultaneously opening the refrigerator, it's easier to send a human tester to perform manual testing. Because developing automation, at the initial stage, will be expensive. A person will look, turn handles and "twistables", record problems and send them to developers to finish.

At some point, when product development is complete and we move to conveyor production, it won't be possible to manually test thousands of refrigerators. Full automation is still needed. A robot will turn handles and press buttons. Yes, such a robot itself is not a simple product, it also needs to be developed and... tested!

**And really, who tests... tests and automation?**

In general, products for testing can be very sophisticated, and their development can be handled by entire companies, with their own testing!

Another note: it's impossible to completely get away from manual QA, somewhere it will definitely have to be present!

---

## QA Part 4: Pessimists vs. Optimists

What's the difference between a tester and a coder (programmer)?

One difference is how each relates to product quality, number of defects, and compliance with specifications and customer expectations.

* **Tester:** Obviously the new version of the product contains many bugs, and in general, this program is probably not working. Now I'll find obvious defects and "lay down" the program (meaning crash).

* **Coder:** Sure that now I've fixed the last error, the program will run "like native", and clients will "drool" and line up just to touch the most "beautiful" creation!

Well, in general, I think you can guess that tester-pessimists usually turn out to be right! Again bugs, crashes, deviations from specification, freezes, sending Tesla into space instead of making a cup of coffee, etc.

Do you pessimistically relate to program correctness? Do you think there are definitely errors and problems hidden there? If you notice something strange, do you continue to "dig" and find serious problems? Do you get some pleasure when you identify unpredictable and inadequate product behavior?

**Well, there's a chance that the tester profession will appeal to you!**

As you may have noticed, this has little to do with education or diplomas. Even programmers (BSc in Computer Science graduates) may prefer to work as testers. It all depends on what attracts you more.

For example, coders are more "turned on" by creating new virtual worlds, their own rules and abstract entities. Programmers won't enjoy sitting and finding all bugs to the last... in someone else's product/code (well, with rare exceptions).

How to increase your chances of finding a tester job? In the next post, and we won't talk about courses! 🙂

---

## QA Part 5: Tips for Job Search

You've completed a Manual QA course, seem formally ready to test software. You can read Test Case Specification (step-by-step test description), and maybe even execute it. You know some Bug Tracking System (where to send descriptions of found defects). You have a certificate about completing the course (month-long? two months?).

**What are the chances that a potential employer will be interested in your modest resume?**

Since the requirements for successful completion of such courses are not high, employers' expectations for graduates of such courses are also corresponding. Easy to complete a course means many similar candidates. And all with "empty" resumes!

Well, not quite empty, some candidates add non-existent experience, internship. Someone might have actually looked at some programming language. Such resumes will stand out somewhat among the general mass of candidates.

**How do you stand out?**

For a moment, let's recall how programmers look for work: besides diplomas and experience, they also try to participate in some competitions and open-source projects, that is, they program for pleasure, gaining skills and the opportunity to somehow show up somewhere.

With manual testing, you can't really accelerate with external projects, but something might work!

Applying to some company? Study their website and products... **for defects!** What if you find some?! Here's an additional plus! Accompany your resume with a short Cover Letter — not necessarily official! A couple of lines about "you have a passion for testing and products of this dream company" is enough, and "look, you have something that can be improved here!".

If you've dug somewhere and found potential defects, try applying to that company. How many bugs there are in Facebook!

Good luck!

---

## QA Part 6: Is $300K a Year Real?

In one group, I came across an advertisement for another QA course. Of course, the course authors point to the average salary of their graduates as high as 100 thousand USD per year!

I would like to immediately warn that statistics allow very easy manipulation of data and getting any result you want. Want $100K — it can be done!

Needless to say, salary depends on parameters such as location, remote or onsite, manual or automation, did the graduate have some technical background before QA school? And how were those who left the course, didn't finish, searched for work for a long time, didn't find a position, etc. counted! In general, if you need to get 2 + 2 = 5, statistics can arrange that for you!

In reality, most likely, most QA course graduates will search for their first job for a long time, and they better lower their expectations about the first salary. But that's not quite what this is about now.

This advertisement reminded me of another long-standing public dispute with one head of such QA schools. Then the dispute reached the point where the opponent threw me a link about salary statistics at **Netflix for a Dev in Test position at $300K**.

Those who know how Netflix hires and pays, and what Dev in Test is, will immediately understand the complete absurdity of this situation.

For the rest, I'll explain why this is a very serious miss. By the way, upon realizing all the stupidity, the disputant deleted everything and no longer made such loud statements.

So what's it about?

The Dev in Test role is not QA, and not even QA Automation. A somewhat closer position to this: QA Infrastructure, but even that's not quite it.

The key point here is "Dev...", that is, we're talking about a Developer, that is, this is a position for programmers! Dev in Test develop testing systems, sometimes these systems are no simpler than the main product itself, and these systems also need to be tested by someone!

It gets worse, Netflix is a company that pays very high fees. It's not so easy to get in. They usually offered a flat rate, so salary is cash, without stocks and bonuses. And yes, if they took you, salaries could reach $250-500K per year! Well, that's if they took you!

Working at Netflix is very stressful, it's not a relaxed Google or sleeping Microsoft, at Netflix they work a lot, and they fire even good programmers for "Underperformed" often and very quickly!

But that's not all!

**Netflix hires engineers only for senior positions**, that is, you need 5 years of experience, and they practically don't take fresh-grads!

These are all obvious things for those familiar with IT, but somehow not for that QA school creator (I don't even remember who it was exactly).

Be careful, dreaming is good, but sometimes you still need to return to reality.

---

## QA Part 7: Black Box vs. White Box

### Black Box

The tester performs tests, simulating possible user actions, performs manipulations with the product, while not using additional knowledge of how this product is developed. That is, information about the internal contents of the product is not used — we consider the product as a "black box". What and how is done inside — we're not interested.

This type of testing is standard. Tests are written, we do everything step by step, record results, submit reports on found defects.

### White Box

The tester knows (approximately) how the product is created, is aware of implementation features, and having this additional information, tries to find defects. This is a more interesting and advanced type of testing. It's necessary to have some level of understanding of the product internals and be able to predict anomalous program behavior.

After talking with developers, familiarizing yourself with the product's architecture and implementation, you can come up with very interesting test scenarios and, in the end, stump the entire programming department. And if you familiarize yourself with the code a bit... you send a bug and immediately point to the line in the code that is the cause of the defect! Of course this is not part of the tester's job, but some QA engineers go that far.

### Exploratory

Exploratory Testing is used... when tests haven't been written yet or there's no time for it. The tester turns on their imagination and tests where they expect to find errors. This type of testing is also used later, during major releases, because surely simple, predictable errors are fixed first, and tricky defects might not have been thought of.

This type of testing can be combined with both Black Box and White Box. Either you study the product and look for errors without knowing the internals, or you have full access to implementation and documentation.

### Gray Box

A middle ground between Black Box and White Box Testing. We test the product, having access to documentation, but don't go looking at the implementation.

