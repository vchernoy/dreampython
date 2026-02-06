# Programming Languages Overview

## Part 1: Fortran, JS

Let's start the overview with completely different programming languages: ancient Fortran and modern JavaScript.

Fortran ⏤ was created in the late 1950s. Creation goals: numerical computations. Fortran was used for mathematical calculations in applied sciences.

At the moment, the chances of landing a position where Fortran might be needed ⏤ are extremely small.

So why did I decide to mention such a dinosaur, and even start this overview with it?

* First, Fortran continues to develop, new standards Fortran 90, 95, 2003, 2008, 2018 have been adopted.

* Second, this language is still quite popular (in its circle).

* Third, Fortran has occupied a certain niche (numerical computations) and is firmly stuck there.

Fortran ⏤ is an example of how a certain technology (programming language) can occupy a certain niche and remain there forever. Often other languages are compared to Fortran in this way.

### Scripting Programming Languages

Usually this class includes: JavaScript, Python, Ruby, PHP.

JS (JavaScript) ⏤ was created in 1995. JS ⏤ is another language that has its own clear niche. JS ⏤ is primarily WEB programming and UI (user interface). In fact, this is an example similar to Fortran: it's unlikely that anyone can seriously push JS out of its field.

It's worth noting that JS is not just a language for UI, JS ⏤ is an entire ecosystem of various technologies that allow rapid development of full-fledged WEB applications.

JS can be found in many, especially young, companies (in startups) ⏤ where there's WEB, there will be JS in some form.

Many coding bootcamps build their courses based on JS, this allows students to create full-fledged projects.

---

## Part 2: Python, C/C++

Python was created in 1991 with the goal of writing scripts. The name was invented in honor of the British comedy TV show: "Monty Python's Flying Circus".

Python and JS are somewhat similar in characteristics and even have some overlap in use in WEB programming. Both languages can be used to write the internal part (backend) of WEB. But unlike JS, Python is not used in developing the interface part (frontend) of WEB.

If you need a full-fledged WEB application, then the interface is written in JS, and the internal part in JS or Python (or many other things). That is, although Python is used in WEB, this is not its main niche.

So where is Python the "Fortran" of its time?

There are several areas where Python sits quite firmly: infrastructure building (DevOps), testing (automation), and it seems the real niche: numerical methods, statistics, data processing, AI/ML.

It seems Python is the modern Fortran — both are used for mathematics, only Python is more for artificial intelligence.

If we take coding bootcamps that teach Python, then most likely there will also be JS for writing interfaces (WEB frontend), and Python will be used for everything else.

### C/C++

The C programming language was created in 1972 for developing the Unix OS (operating system). This is a compiled language and completely unlike JS or Python.

In its time it had very important properties: could be used on different platforms. At the moment, despite obvious obsolescence, C is very deeply stuck in areas of systems programming: OS development, compilers (of other programming languages), embedded systems, etc. For example, the first versions of Python were written in C.

The chances of working with C or at least getting acquainted with it exist only for students and graduates of computer science specialties, and even then not in every university.

C++ appeared in 1983 as an extension of the C language. Both have similar goals and are used in the same areas. For our overview, it's not so important how they differ.

It probably makes sense to mention such a feature: C++ is much more complex than C. The description of the C language takes a couple of hundred pages, while the description of C++ is thousands of pages, and very complex text at that.

Finding a pro who would know 99.9% of C++ is not so simple, most likely such unique individuals sit on the standardization committee of the language itself.

In general, neither C nor C++ are found in three-month courses, even in half a year it's unrealistic to substantially get acquainted with even C, not to mention C++.

---

## Part 3: Ruby vs. Python vs. JS

Ruby was created in 1995 ⏤ in the same year as JS (JavaScript). Ruby's main niche ⏤ is server-side WEB programming, so it's reasonable to compare it with other competitors: Python and JS.

Ruby ⏤ is a younger language than Python, but for developing the server part of WEB applications, Ruby offers a more advanced platform: "Ruby on Rails". The Python framework: Django was released later and didn't get such distribution.

Although Ruby has potential, besides WEB, it hasn't yet conquered serious positions in other areas. Partly this happens due to a more compact community than Python.

If we compare Ruby with JS, then the latter offers a much larger number of platforms: Node.js, React, Angular. Also, let's not forget that JS dominates in the client part of WEB, where actually neither Python nor Ruby are competitors to it.

Obviously we have that if we want to develop a WEB application (front-end + backend), then we can stay within JS, or we can choose Ruby (or Python) for backend/server-side, and use JS for front-end/client-side.

By properties, these three programming languages are somewhat similar, but probably Python will be somewhat easier to learn. Although if the goal is to get into WEB front-end, then JS is essential. In coding boot camps, you'll most likely encounter a combination of these programming languages and their frameworks.

---

## Part 4: Java

Java was also created in 1995, but by goals and properties it differs very strongly from JS, Python, Ruby. Java is more like something in between C++ (remember this monster) and Python. That is, the barrier to entry into Java is much higher than Python. The description is huge, packages, platforms are a sea, but it's not as scary as in C++.

If we recall a bit of history, Java was created by Sun company with the goal of pushing Microsoft company out of its sphere. This didn't particularly help. Sun was bought by Oracle, and Microsoft released its Java analog for Windows: C# (the .NET platform).

Initially Java was presented as an embedded OS, like all teapots and irons will "speak Java" (does this remind you of anything?). But now of course everyone has forgotten about this.

At the moment, Java is widely used in developing WEB applications and applications for mobile devices (for Android OS). Also Java can be found in testing, infrastructure, data processing and even in AI.

Java — almost everywhere, and remains one of the most popular languages. But most likely you'll encounter it in older large corporations. Young companies and startups will prefer either something from the trio Python, Ruby, JS or some newer technologies.

Although Java's positions are still strong, direct successors and various competitors are gradually putting pressure on it: Scala, Kotlin (for Android), Golang (WEB), Python.

---

## Part 5: From Java to Scala and Kotlin

Let me remind you that Java ⏤ is a general-purpose programming language. By syntax it's more similar to C/C++/C#, but simpler and cheaper to use. Java in complexity is somewhere in the middle between the excessive complexity of C++ and the compactness of Python.
Java is also used in such areas as: testing, infrastructure, AI and in developing mobile applications for Android. It's worth noting that under Android a somewhat specific version of Java is used. So even having experience in Java development, you'll have to spend some time studying the Android OS itself and the Java for Android version (based on older Java standards).
Modern programming languages Scala and Kotlin develop the Java platform in different directions, maintaining full compatibility with it. In Scala projects you can use Java code. The same is true for Kotlin.

### Scala

Scala development began in 2001 within the walls of an academy in Switzerland, and the public release took place in 2004.

Scala initially constantly broke backward compatibility with older versions. This created huge problems for adoption of this platform by large companies. On one hand, everyone was ready to run anywhere away from fading Java, and on the other hand, transitions to new Scala versions could stop projects for an indefinite time.

Some large companies completely abandoned Scala in favor of Java, for example, LinkedIn. At the same time, Twitter company pushed Scala forward, despite any problems.

At the moment, Scala releases have more or less stabilized, but Scala's development also gave impetus to Java's development. So as a result, a stormy transition from Java to Scala never happened.

The main difference between Scala and Java: reduction of verbosity. Programs in Scala are more compact than similar ones in Java. Write less, read better ⏤ fewer errors, sort of like that. In principle, in this sense, Scala has the same idea as Python ⏤ do everything as short and simple as possible.

But on the other hand, Scala is such a powerful language that you can create your own DSL (domain specific language) there. That is, you can write such a program in Scala that without additional "hints", even the coolest Scala specialist won't figure out what this is in front of them.

### Kotlin

Kotlin was developed by the Russian company JetBrains in 2011. The authors wanted to create something "like Scala, only faster, simpler and for Android". And they did it!

In 2017, Google company, which owns Android OS, announced full support for Kotlin as a platform for developing mobile applications for Android.

So if you want to develop mobile applications for Android, you can start directly with Kotlin. Everything will be both faster and simpler. Although at some point, you'll have to look at Java (including Java 1.6) and be a bit horrified.

Of course, various boot camps and courses are available, teaching Android App development on Kotlin from scratch.

