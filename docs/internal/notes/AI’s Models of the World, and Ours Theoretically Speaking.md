(background chatter)

[AUDIENCE MEMBER TWO]
All  

right.

(background chatter)

Yeah. Feel free to come to the seats 
at the front, if you're standing.

(background chatter)

Right. Let's get started. Good evening.

It's so great to see a packed house at 5:30 PM. My 
name is Venkat Guruswami. And as director of the  

Simons Institute for the Theory of Computing, it 
is my great pleasure to welcome you all to today's  

Theoretically Speaking public lecture titled AI's 
Models of the World and Ours by Jon Kleinberg.

A bit of introduction about the Simons Institute, 
we are the leading international venue for  

collaborative research in theoretical computer 
science. Established in 2012 with a generous  

grant from the Simons Foundation, the institute 
brings together world's foremost researchers,  

as well as the next generation of outstanding 
young scholars for sustained collaborations  

on thematic programs that span not only the 
foundations of computing, but also its interface  

with the sciences, mathematics, technology, 
and society. Alongside our research mission,  

we seek to foster public understanding of 
algorithmic science and its ever-expanding  

influence on our lives through communication, 
outreach, and events such as this one.

In that spirit, today's lecture is part 
of our Theoretically Speaking series which  

aims to highlight exciting advances in the 
theory of computing for a broad audience.  

And if you're active on social media, 
we invite you to live post this event,  

and use the hashtag hash #SimonsLive and tag us 
at Simons Institute, so if others are interested,  

they can find and follow the conversation. And 
before I introduce today's distinguished speaker,  

I would like to acknowledge the generous 
support of the Simons Foundation and Simons  

Foundation International, as well as 
our industry partners and individual  

donors which makes our research mission 
and events such as this one possible.

With that, it is my-- now my honor to 
introduce today's speaker and one of my  

personal academic heroes Jon Kleinberg. Jon 
Kleinberg is the Tisch University Professor  

in the Departments of Computer Science and 
Information Science at Cornell University.  

Jon's work has shaped multiple areas 
across computer science, from algorithms  

and networks to the ways they interact with 
large-scale social and information systems.

His research has illuminated how 
technology-mediated systems function,  

for example, how information propagates, how 
networks evolve, how algorithms make decisions,  

and relevant to today's talk, how AI 
models represent their knowledge and  

so on. His work is characterized by a 
remarkable ability to distill complex  

real-world computational phenomena into crisp 
theoretical questions, and his models have  

a knack of capturing the essence of these 
phenomena with just the right abstraction,  

yielding insights which are both mathematically 
profound and at the same time deeply relevant  

to how modern information systems shape our 
world. His writing reflects the same clarity.

Jon is a co-author of two highly influential 
textbooks, Networks, Crowds, and Markets,  

which helped lay the foundation of network 
science for a broad scientific audience,  

and the widely used algorithms textbook, Algorithm 
Design, which has shaped how generations of  

students learn to think algorithmically. Now as 
for Jon's awards and honors, if I list them, we'll  

be here well past dinnertime, so just a small 
sample, I will mention the MacArthur Fellowship;  

the Nevanlinna Prize, which is now called 
the Abacus Medal; the ACM Prize in Computing;  

the World Laureates Association Prize; and 
election to both the National Academies of  

Science and Engineering. Jon is one of 
theoretical computer science greatest  

ambassadors, and it's our pleasure to host 
him again in this public lecture series.

So please join me in welcoming  

Professor Jon Kleinberg to the Simons 
Institute's Theoretically Speaking.

(applause)

[JON KLEINBERG] 

All right. Yeah. Thanks very much for 
the invitation to come speak here.

And yeah thanks all of you for 
turning out at this evening hour. Um,  

it's it's always a pleasure to come speak at 
the the Simons Institute. And it's-- I mean,  

it really has, just as someone who is 
a, you know, a frequent visitor to it,  

just been really a sort of a hub of activity 
and sort of an intellectual beacon for the  

theoretical computer science community, both 
for all of its, you know, I think internal  

activities, all of the kind of theory-focused 
activities that have gone on here, as well as  

its outreach into the sciences and academia more 
broadly, and also to industry and civil society.

I think it's really it's been a-- A great 
resource which we're really grateful for all  

the effort that people here at Berkeley have 
put into it, as well as, of course, to the  

Simons Foundation. And you know, and it hosts 
events like this which bring us all together.

So I wanted to talk about some things that 
a group of us have been thinking about with  

regard to AI and how it interacts with the 
world. Um, this is gonna be joint work with a  

whole set of people listed here, and I'll, I'll 
try to kind of introduce them gradually as we,  

we grow through things. I guess for sort 
of thinking about this topic, it's useful  

to go back some distance and think about, you 
know, why are, you know, how did we get here?

And so let's start with the internet, which 
all of this is built on. What's interesting,  

of course, about the internet, we're now 
sort of in the maybe 30th or so year of  

the sort of widespread public use of the 
internet, somewhere between 30 and 35 years,  

depending how you count. And one thing that's 
been interesting in that period is the way  

in which the metaphors that we've used for 
the internet have evolved over time, right?

So if you go all the way back to, you know, 1993, 
'94 when the first graphical web browsers came out  

you know, if you had asked, you know, me in grad 
school at that point or other people, you know,  

"How do you think about the World Wide Web or 
the internet?" I think we would have used this  

metaphor of the library, right? It's a vast 
universal library of all human knowledge.

We put the knowledge online, and 
we've linked it together. And that  

sort of would have been how we thought 
about it. And that metaphor, I think,  

worked pretty well for guiding how we approached 
things on the internet for a good 10 years.

But then there was this really formative period, 
2004 to 2006 when people sort of stepped out from  

behind their web pages and began interacting 
more directly. They began uploading photos  

much more actively. They posted and commented 
on what we eventually called social media.

They tagged people in images. And so this 
metaphor of the crowd began to kind of merge  

with the metaphor of the library, right? 2004 to 
2006, right, was s-- sort of such a compressed  

window that that was in sort of a three-year 
period, the creation of Facebook, YouTube,  

Twitter, the iPhone, right, all of that in this, 
in this really formative 2004 to 2006 period.

And that went on for a while. And I think 
actually for a while people said, "Okay,  

this is, this was the answer. This 
was what the web was all about."

It was really about unlocking human capability. 
Because in some sense, you know, you can think  

about computing as in always involved in this 
very slow pendulum swing between two views of  

what computing is, right? Computing is either sort 
of, you know, a enabler of human capabilities,  

or it's a means of automating things so that they 
can, you know, be done without humans present.

And that pendulum swings back and forth on 
a very long time scale. And in 2004 to 2006,  

we're like, yes, this really, the web was 
really all about unlocking human capability,  

which it assuredly is. But there 
was one more twist of the pendulum,  

which was in 2012 to 2014, again a really 
rapid three-year period of enormous advances.

Um, the power of deep neural nets combined 
with huge datasets suddenly caused us to really  

achieve massive performance improvements, many of 
which occurred, you know, here at Berkeley and in  

the Bay Area more generally, on 50-year-old 
problems in the field, right? Recognizing the  

objects in an image, turning a sound signal into 
transcribed text so as to do speech recognition,  

summarizing documents written in natural language, 
right? All these problems that the field had very  

much wanted to solve were suddenly seeing 
these enormous performance improvements.

And in a way, it was partly, and, you know, 
I mean, there were computational advances,  

but there was also the fact that all 
that data people been putting on online,  

all those photos people had uploaded were 
the training data for these algorithms,  

right? A bunch of things that we had 
wanted to do in the '80s and couldn't do,  

the people doing them, you know, trying 
to do them in the '80s assured us that  

if only they had 100 billion labeled images 
instead of 10,000, right? If only they had  

maybe seven orders of magnitude more data, 
this stuff would really all start working.

And, you know, in the 1980s, how 
are you supposed to audit a claim  

like that? I have no idea. But roughly 
speaking, that's what happened, right?

The field took this 20-year-long 
detour. Crowds entered the internet,  

tagged photos. They said, "This is my friend.

This is a car. This is a tree." 
And 100 billion images later,  

a bunch of things started working in 
ways that they simply hadn't before.

So actually, for those of 
you keeping score at home,  

if you really believe these things move in 
10-year increments, we're kind of at the  

end of yet another 10-year increment. So you 
can ask yourself, you know, you can ponder,  

is there some fourth thing? Or maybe this third 
thing is the last thing we're ever gonna have.

Who knows? So algorithms have 
become powerful because of two,  

these two reasons, massive computational 
resources and this massive amounts of data  

that we have all collectively put online. And 
so it causes us to really ask the question,  

you know, when an algorithm looks out at all 
of that, what is it actually seeing, right?

How does an algorithm see the world? And 
there's a lot of metaphors that go on here.  

I often do find it useful to think of, you 
know, the algorithm is in some sense this  

hyper-intelligent alien that can 
analyze enormous amounts of data,  

do enormous amounts of computation, but 
it does not really live in the world.

It does not, you know, it observes the world, 
and it tries to figure out things about the  

world by looking at this data. And I realized when 
I sort of began to ponder these metaphors, and I,  

I think I probably began pondering them as all 
this data came online circa 2004 to 2006, that I'd  

actually sort of heard this thought experiment 
before but not in a computer science context.  

Um, rather when I was an undergrad at 
Cornell one of Cornell's big exports to  

the world at the time was Carl Sagan, 
the, the, the famous astronomer and  

one of the 20th century's most notable 
popularizers of science for the general public.

And Carl Sagan sightings on campus were quite rare 
because he was off and traveling around doing the  

kind of Carl Sagan-like things that he did. And so 
when he gave a lecture on campus, people showed up  

for it. And so in spring of 1993, he gave this 
talk with the title, Is There Life on Earth?

Kind of a, a strange title based on a paper he 
had published in Nature with the only slightly  

less strange title, A Search for Life on 
Earth from the Galileo Spacecraft. Now,  

it turns out Carl Sagan had been asking this 
kind of question, is there life on Earth,  

for his whole career. You can find papers by him 
in the '60s about this and the '70s about this.

What did he mean by this? Well-so he was often 
sort of organizing these joint Cornell, JPL  

missions to the outer solar system, looking for 
evidence that there was, you know, maybe once life  

on the moons of Jupiter or Saturn, right? Maybe 
once Titan or Europa actually had life on it.

And so they would fly these space probes 
out there. Um, and in, in this case,  

they were flying the Galileo spacecraft out to 
kind of do these measurements to try to detect  

weak signals of life on, on, or maybe there 
was once life on these moons. And the way these  

missions go is you fire this thing, you have to 
get enough speed to go to the outer solar system.

So you fire it toward the sun and it slingshots 
around Mercury, picks up speed, and goes to  

the outer solar system, which means that at some 
point, it's passing back over the Earth on its way  

out toward Jupiter and Saturn. And so Carl Sagan 
asked the question, you know, if we're gonna try  

to detect life on the moons of Saturn and Jupiter, 
faint traces, probably as a dry run, just as, as  

a good double check on our instruments, we should 
be able to detect the presence of life on Earth.  

Like, if we can't do that, probably this mission 
does not have a really big chance of succeeding.

And so in his lecture, he used the metaphor 
of aliens, right? Because just as algorithms  

looking at the, at the world are like aliens 
picking up the data, his Galileo spacecraft was,  

at that point, essentially like an alien 
space probe looking down at the Earth,  

picking up physical and chemical measurements, 
trying to figure out can it detect life? Right?

So he asked if we were aliens and we had this 
data, would we recognize something anomalous  

about the Earth that might tell us there 
was life? Now his questions were sort of  

physical and chemical and not germane to this 
talk. Uh, for those of you who are curious,  

certainly one of the notable things about Earth 
is that there's an enormous supply of diatomic  

oxygen existing right next to flammable gases 
like methane, which should not happen, right?

That should all combust and just be gone 
and become water and carbon dioxide. The  

fact that it's there suggests something 
very complicated is replenishing diatomic  

oxygen into the atmosphere. That 
was certainly one of his big tells.

Um, anyway, so let's think about this life 
on Earth question. So around the birth of  

social media, a group of us Lars Backstrom, Dave 
Crandall, Dan Huttenlocher, and I began to try our  

own life on Earth experiments with somehow, with 
some of the early social media sites circa 2004,  

2005. And one way to do this is to go back to 
some of the early photo sharing sites, right?

When photo uploading and photo tagging was first 
a thing, and look at how they were displayed on  

the Earth, right? So you could take, for example, 
a black screen here, and you could go to a 2005  

era social media site where people were 
first uploading photos and take the latitude  

longitude of every photo that was uploaded 
and just put a white dot on the screen. Okay?

So just a big pattern of dots where every 
photo was uploaded. And when you do that,  

you get a shape that looks like 
this, right? And of course,  

the fact that you see a map 
there is only in your mind.

It's really just a pattern of dots. But it 
is certainly true that people take photos  

up to the edge of the water and many fewer 
of them take photos after that. Similarly,  

you see these particularly bright 
spots at like cities of the world.

You see long strings where there are rivers,  

interior seas. You see a bunch of things. 
Now, we begin to notice a few things.

Obviously, first, I'm only showing about 40% 
of the Earth's area here. I'm not showing the  

whole Earth. But also, this is not, obviously, 
this is not the population density of the Earth.

There are incredibly densely populated 
areas here, here, there that simply were  

not on this particular social media site in 
2005. They weren't using it. So, you know,  

and this of course is, you know, something that 
we see, you know, whenever anyone talks about  

biases in the training data, this is certainly 
a key example of bias in training data, right?

This is not the Earth. This is the 2005 era photo 
uploading portion of the Earth, right? And even  

the parts that are heavily covered, like this 
is not the population density of the Himalayas.

These is all the people who went and climbed 
the Himalayas and later uploaded their photos,  

to social media. And of course, 
there are also artifacts in the data,  

right? So if I were to extend this 
picture just a little bit south here,  

kind of right here, there'd be a really bright 
dot you know, like all these bright white dots.

A really bright dot kind of in the Atlantic, 
in the curve of Africa, there, kind of South  

of Accra, West of Libreville. And you look at 
that, and you say, 'I wonder what that is,' right?  

And the answer, if you've played with geo data, is 
that there are a lot of phones, certainly in 2005,  

there were a lot more phones, that when you 
uploaded it, they didn't report their lat long.

Instead, they reported 0, 0. And where is 0,  

0? It's where the prime meridian intersects 
the equator, which is right there, right?

So you have to notice these things in 
the data, right? Some of it is actually  

just kind of anomalous. So this 
data was like pure signal, right?

It was sort of amazing how much you could 
get out of things like this. You could say,  

for example, take the 100, or say the 
20 densest 100-kilometer circles and  

take the textual tag in there that's the most 
anomalous, right? Not the most frequent, right?

The most frequent might be trip or family, 
or vacation, but the one that deviates the  

most from its background distribution over 
the whole world, right? As people say trip  

and family vacation all over the world, but only 
when they're staying at the base of the Eiffel  

Tower do they say Eiffel Tower. And then you can 
take 100-meter disks within each one, the distance  

which you can see something and take a photo, 
and look for the most common word there, right?

And then you get these hotspots, right? 
And so, for example, from this 2000,  

already in 2005, and remember, this entire 
site had fewer photos than are uploaded in  

one day of social media now, right? 
So it was both a huge amount of data  

and almost nothing by the standards 
that we're talking about now, right?

And so you get the 20 most common, the 20 tags 
of the densest things here. And for each of them,  

you know, the four densest 100 meter 
circles within that city and the names  

assigned to them. And again, almost all 
of it is highly meaningful here right?

There's incredible amount of signal 
compared to the noise. I mean,  

we could debate whether the Apple Store is truly 
the fourth most important landmark in Manhattan,  

but apparently to, if you were a user 
of the social media site in 2005,  

it was like a pilgrimage to go there, take a 
photo of it, and upload it and tag it. And so  

it's a reminder that these 100 meter disks with 
the names attached are hovering over these things.

It's the beginning of every alien invasion 
movie you've ever seen, where one morning you  

wake up and the flying saucers are over the 
Eiffel Tower and the Empire State Building,  

and the reporter stands there puzzled and says, 
"We don't know what they are. They just showed  

up this morning." And you wonder, "How did they 
know to hover over all those famous landmarks?"

And maybe for the aliens, it's not as 
hard as we think it is. So, the point is,  

this is the data that we're building 
on. And one of the key things about  

computing is the extent to which it works 
based on abstraction barriers, right?

I think this is one of the really powerful 
theoretical constructs that goes back to the  

very early days of computing that if you 
can find the right abstraction barrier,  

then you can separate the low-level implementation 
of the technology and all the reasoning about that  

from the applications that you build on 
top of the technology. And so on the one  

hand beneath. And so often people think of this 
as like the metaphor of the hourglass, right?

There's a lower lobe of the hourglass where we 
build all this sort of conceptual infrastructure  

for how to create these algorithms, and then 
there's the upper part of the hourglass where  

we build on top of that technology, and as long 
as the two parts agree on a consistent model,  

right? So, a consistent model of the shared memory 
computer, the Turing machine, the Boolean circuit,  

the distributed system, right? These are 
constructs that we create so that the people  

working down here can communicate with people 
up there by exchanging very little information.

If you know that you're building a chip that 
implements the shared memory computer abstraction,  

then someone writing a high-level programming 
language or programming in it can program to  

that high-level abstraction and they'll 
meet in the middle. Okay. And so this  

is the substrate on which many of these 
AI applications are being built, right?

Huge amounts of data and machine learning 
algorithms down here, these AI applications  

up here communicating through this very thin 
interface in the middle. Now that brings us to  

the present, to super powerful AI. And obviously 
there's a lot of, you know concern about, concern,  

interest, fascination, all of these emotions 
about, you know, what these things are capable of.

And you see discussions of, you know, if 
AI were to become superhuman in domain X,  

what would that look like, right? So what 
would it look like if we had superhuman  

AI doing mathematics or making legal arguments 
or making medical judgments or composing music  

and so forth? And these discussions 
are, on the one hand, fascinating.

On the other hand, they turn 
immediately speculative. We  

don't really know what's going to happen if we're  

in those situations. It's certainly wise 
to sort of think ahead and be prepared.

But if we really wanna think ahead, then 
there's something else we could also be doing,  

which is to look for a domain 
where this has already happened,  

right? Where we don't have to guess what 
would happen in a world of superhuman AI,  

but where we simply have it. Now we 
wanna choose our domain carefully, right?

I think adding up long columns of numbers is a 
domain in which computers were superhuman for a  

long time, but it doesn't fascinate us because we 
never thought of adding up long columns of numbers  

as special to us. So what we really want is some 
kind of creative pursuit in which algorithms have  

conclusively surpassed human abilities, and yet, 
it has the property that people, in this area,  

it's a sort of aesthetic human creative 
activity. People train their whole lives,  

achieve this level of mastery that inspires 
a sense of awe in other human beings where  

you can have whole libraries filled 
with a century or more of scholarship.

And yet despite all of this, this mastery, 
this training, this scholarship, despite that,  

computers have simply surpassed human beings, 
right? And arguably a sort of key example of this  

is chess, right? Chess is a domain which 
certainly is a, you know, sort of a pinnacle  

of human creativity up there with, you know, 
music composition and literature and so forth.

And yet where if the goal is to win chess 
games humans have long since been surpassed.  

Now lots of people have worked on chess as a model 
system, right? Newell and Simon worked on chess.

Claude Shannon, pictured here giving 
a prize to the creator of Deep Blue,  

worked on chess. Deep Blue famously defeated 
Garry Kasparov, the world champion, in 1997,  

which was sort of a, a moon landing 
type event for it. In some sense,  

like chess has long been a model 
system for decision making.

It's one of the few things to have been 
metaphorically called the Drosophila of  

more than one area, right? The Drosophila, the 
fruit fly, the organism that's so malleable  

that it can be the model system for genetics, 
and metaphorically chess has been called the  

Drosophila of psychology by Herb Simon and William 
Chase, the Drosophila of AI by John McCarthy. Um,  

but now it's sort of the Drosophila of one 
extra thing, which is of superhuman AI.

So, knowledge of chess will not be necessary for 
this talk. You can just think of it as a human  

activity where there's a lot of, you know, just a 
lot of human mastery that's occurred over the past  

century. But just as a brief timeline, computers 
just kept getting better and better at chess.

And the late '80s, early '90s were this 
interesting period which sort of eerily  

evokes some of the things that you hear now, 
where they began defeating human grandmasters,  

right? They were now beating all 
but the best hundred people in the  

world. And people sort of were still skeptical.

1992, '93, they're like, "Yeah, I see that 
happening, but I think there's something  

special about the best few human 
beings that they're just not gonna  

get defeated by computers. Everyone 
else will get defeated by computers,  

but not the best few human beings. 
There's something special about them."

Which was just objectively false. The 
computers just kept getting better at a  

pretty steady rate. And, you know, so the famous 
match between Deep Blue and Garry Kasparov,  

in which Deep Blue won, it was 1997.

For five years, there was this interesting 
activity where the best humans in the world  

would play the computer on roughly equal terms. 
But 2005 was the last time any human being ever  

sat down from a computer, across from a computer, 
say, as powerful as my laptop, and beat it or even  

drew against it. It's simply they are now 
just, and they kept getting better, right?

They were on a growth curve, 
and that was not, you know,  

the world kind of lost track of what was 
happening, but they just kept getting better,  

better, better. Okay. We could also 
express this in terms of numerical ratings.

You know, I, you can think of, like, amateur chess 
players, people who play chess as a hobby. Most of  

their ratings range between the numbers 1,000 and 
2,000, right? Numerical rating, higher is better.

You know, a player who's 2,000 is a very, very 
good amateur chess player. And then, you know,  

by the time you get to, like, 2,400, 2,500, 
your friends are saying, you know, "Have you  

considered playing this professionally? 
2,800 is the best player in the world."

And current chess engines are well 
beyond 3,300. It's actually hard to  

evaluate ratings up there. It's probably 
like 3,600, somewhere around there.

Right, so there, and differences are kind of 
translate in variance. So, 3,600 to 2,800,  

they're as far beyond the best humans as 
the best humans are beyond like amateurs  

who are pretty good and play on weekends, 
right? That's how far beyond they've gotten.

Okay. So the question is, this is an activity 
where, again, if the goal was to win chess games,  

it's, computers are far, far 
beyond us. So what happened, right?

It's fair to ask, can we derive any 
stylized facts from observing chess? Now,  

obviously every domain is different, right? 
Chess is not the same as mathematics.

It's not the same as medicine. First of 
all, it's a game. People do it for fun.

But it certainly has some of the 
characteristics. And so here are  

some stylized facts that I think are sort of 
interesting to keep in mind. Four of them.

So one, chess as an activity is as popular 
as ever, actually more popular than ever. Um,  

that's because of some other features 
of the internet, such as live streaming  

of chess games on Twitch and YouTube the 
availability of enormous amounts of, like,  

online play. You can find people to play with 
all around the world on sites like Lichess.

Now we could ask, other activities 
might not remain as popular as ever  

when AI becomes superhuman, because 
we don't particularly enjoy doing  

them. And we're happy to delegate to 
algorithms. Chess is something we enjoy.

But it's certainly-- it was not the end of chess 
when algorithms became superhuman. A second point,  

which I think is actually showing up in many 
domains where AI is beginning to surpass or  

match people, this principle that the spectators 
now know as much as the participants, right? So,  

this kind of democratization of expertise, if 
you want to call it that, where somebody watching  

with a chess engine turned on suddenly knows as 
much as the expert sitting at the chessboard.

So much so that things have been dramatically 
inverted, right? So in 1980, if say, you know,  

or, you know, 1985, Kasparov sits down from Karp-- 
across from Karpov in a world championship match,  

they're playing. Afterwards, 
there's a press conference.

They play for six hours, they play a game, they 
come out and there's a press conference, and the  

chess journalists all ask, you know, ask them, you 
know, "Why did you make that move on move 25?" And  

they explain, because the two people in the world 
who understand this game that what just happened  

the best are Karpov and Kasparov. They understand 
it way better than anybody else in the audience.

And so they're here to share their wisdom 
with people. Fast-forward 40 years to 2025,  

people playing the world championship. First 
of all, they're sitting in a sort of soundproof  

booth to prevent, like, cheating because 
people are watching with engines turned on.

And everyone's watching with the engine 
turned on, and they're watching the board,  

and they're wondering like, "Why is he-- why is 
this person not playing pawn to G5? It obviously  

wins," because the engine told them that. And 
they're sort of forgetting that if they didn't  

have the engine on, this would be not at all 
obvious to them and they wouldn't even see this.

And so the fact that they're kind of like yelling 
at their TV, effectively, wondering why this,  

you know, chess grandmaster is not playing pawn 
to G5, it's not nearly as easy as it looks when  

you have the engine turned on. But it also means 
that when the players come out for their press  

conference, and you can watch chess press 
conference, this is actually what happens,  

they ask the journalist like, "What should 
I have done on move 25?" Because the two  

players who understand the game the 
least are the two players at the board.

Everybody else was watching 
with the engine turned on,  

right? There's been a complete inversion 
of the expertise. And I think that's sort  

of an important thing to keep in mind 
as we look at these other activities.

A third one, the aesthetic standard. So 
I, I'll talk about some research I did,  

beginning with Ashton Anderson in around 
2015, coming back to look at chess through  

this lens. And you know, I had played chess 
a little bit in high school, and I came back

And I looked at 2015, and one thing that struck 
me, and I read a bunch of stuff where other people  

had this reaction, that in the 1960s, '70s, '80s, 
like all of classical chess, like the aesthetics  

of the position were a proxy for safety, right? 
It was very hard to calculate chess positions,  

and you didn't have a chess engine to tell 
you what the right answer was. So you fell  

back on sort of aesthetic heuristics, 
along with calculation, you know, rooks,  

and again, knowledge of chess, not crucial, 
but there were certain principles that apply.

Each sport has its own principles. 
And in chess, there are things like  

rooks belong in open files, knights should be 
on advanced outposts, don't double your pawns,  

all this stuff, right? You come back 
in 2015, and the board just looks ugly.

It's a mess, right? Pieces are everywhere. 
It's sort of like if 1970s and '80s chess  

was like this sort of elegant, sort 
of cinematic sword-fighting scene,  

2015 is more like a kind of fight 
with like broken beer bottles, right?

It's like just, it's ugly because what 
happened? They practiced with chess engines,  

and they know that if it works, it works. 
It doesn't matter if it looks good.

They're just going tactically. 
They're going by the calculation,  

the engine showed them. Of course, the more you 
see it, the more its own aesthetic emerges, right?

It's not that there was no aesthetic, it's just 
that the aesthetic had changed dramatically  

because we now had engines to help calculate. 
And again, think about your favorite domain where  

you're worried that AI might be sort of, you know, 
competing with humans. There again is this issue  

that the human aesthetic standard we've often 
had has both been because we value aesthetics,  

but also because we often use it 
as a heuristic to guide our work.

And those heuristics start to erode 
when AI becomes superhuman. Finally,  

something which I'll come back to in much more 
detail, the AI frequently sets you up to fail,  

right? The fact that you're looking at the 
engine going, "How can these people not  

see that pawn G5 is obviously winning?" 
Goes away when you turn off the engine.

Suddenly, you're lost, right? Okay. So 
around 2015, it was occurring to me that,  

like, you know, we have this genuine bona 
fide superhuman activity going on with AI.

Let's study it in various ways. And so I convinced 
Ashton Anderson, a longtime collaborator of mine,  

that we should look at this. And then we joined 
forces with Sid Sen at Microsoft Research.

Ashton admitted a student, Reed McElroy-Young, 
who did a bunch of really exciting development  

on this. And one question that we asked was, 
okay, we have engines that can make amazing  

chess moves in order to win chess games, but can 
we also learn to match human decisions? Right?

Because we might wanna set up moral systems 
where Superhuman AI interacts with human  

capabilities. But if I wanna, for example, run, 
you know, a billion iterations of something,  

humans don't really have the patience 
to sit through a billion iterations  

playing a a superhuman AI, so I need 
a stand-in for the human part of it.  

And so it's natural to wanna train 
something that plays like a human.

And so the goal was simply a prediction 
problem. Given a position P encountered  

by a human player of rating X, predict 
the move the player will make. Right?

I would like to build something that as 
faithfully as possible makes moves like  

a 1,500-rated chess player would do. And so we 
did this. We built a chess engine called Maia.

And the idea was by then, DeepMind had released 
AlphaZero, which had taught itself to play chess  

just from the rules and through self-play. 
The open source community had replicated it  

'cause DeepMind didn't release AlphaZero, but 
they built this thing called Leela, which was  

basically an open source version of AlphaZero 
that also taught itself through self-play,  

also became superhuman. And that the head of that 
neural net was trying to make good chess moves.

So if you take off the head of that neural net and 
you put on a head that tries to, as faithfully as  

possible, make the move that, you know, the human 
1,500-rated player made in the training data,  

then you have a predictor of human moves. And 
so you could make a Maia for each rating, 1,100,  

1,300, 1,500, so forth, and each one basically 
is sort of best at predicting for the rating  

it was tuned to, right? Maia-1100 
peaks in its performance at 1,100.

Maia-1300 peaks in its performance 
at 1,300 and so forth, right? These  

are the performance curves of how 
well it does at matching moves of  

people of each rating. And they're much 
better than the sort of leading engines,  

both Leela, the neural net engine, and 
the leading traditional engine, Stockfish.

All right? So if you're actually trained to 
do this, then you can do much better because,  

of course, right? The alternative is 
I could take a superhuman chess engine  

and just sort of dial down its search all the 
way until it's basically making random moves.

And by some sort of intermediate value theorem, 
if I go from superhuman to making random moves,  

somewhere in between, you will play it 
on even terms. But that doesn't mean  

it's playing like you. It just means 
you win about as often as you lose.

And in fact, it's not playing like you. You have  

to actually train something to 
actually play like you. Okay.

And so the point is, you can do a bunch 
of things with an engine like Maia. We've  

actually been experimenting with it 
for teaching purposes, for example,  

right? It can, for each rating, try to guess 
what a human of that rating would make.

So again, this is the most chess-like 
thing. It's not important if you actually  

follow what's going on in this position. But the 
point is, if you ask an engine like Stockfish, the  

most powerful traditional search, chess engine, 
what to do, it'll say, "Play pawn takes a6."

And Maia predicts that around 1,500 is when 
a player will start playing that. Whereas at  

lower ratings, it'll play the much, much weaker 
move pawn to b6. And so it'll actually try to  

find the point at which you cross over from 
one move to another as the rating goes up.

All right. So we released this on lichess. 
It turned out to become very popular.

As it turned out, we released it right 
at the start of the COVID pandemic,  

people were online playing 
huge amounts of chess. By now,  

it's played several million games. 
Some interesting things, actually.

So the most played version is Maia 
1100. It plays like an 1,100 rated  

thing. We turned it on in a mode where it 
always made the most likely move, right?

So there were sort of two choices 
when you release Maia onto the  

internet. You could either have it 
play, draw from the distribution.  

It's computing a distribution over 
moves that 1,100 rated players play.

There's this probability in this move, this 
probability in this move, this probability in that  

move. It can either draw from that distribution, 
or it could just pick the most likely move. It  

turned out after some experimentation, people seem 
to enjoy it more if we pick the most likely move.

But a funny thing happened, which was its 
rating on lichess was actually around 1,400,  

not 1,100, where it's trying as hard as it can 
to play an 1,100-rated player. That's where it  

has the best move-matching accuracy. And when 
it actually plays games, it plays at 1,400.

And it's an interesting question exactly 
why this is. We have a conjecture that  

we certainly believe in, which is that 
1,100-rated players often lose chess games,  

right? A chess game goes on very long 
time, and one bad move can throw it away.

And those bad moves are often idiosyncratic 
mistakes that they normally wouldn't make.  

So it suggests that if you're rated 1,100 
and you could succeed in always playing the  

move that you were most likely to play, you 
would actually gain 300 rating points just  

like that. You don't actually need to get, 
you just need to avoid the rare mistake.

You can make all the mistake, your typical 
mistakes, just concede those, but avoid  

the rare mistakes, right? This effect goes away 
around Maia 1900. Maia 1900 is rated about 1,900.

And so whatever gain there was seems to be at  

this low end. Okay. Some other things 
that happened once we released this.

So first of all, we can only create Maias up 
to about 2,000, 1,900, 2,000, because there  

just wasn't enough training data for us beyond 
that to try matching. And the problem with it,  

if you start doing, like, actual chess 
engine search, it gets too good. Um,  

but subsequent work, there's continued to be 
improvements all-- all the way up to the present,  

has actually managed to produce really good move 
matching accuracy, so this new system called Alli,  

up to, say, 2,700, 2,800, to play 
like the best players in the world.

We also started to create personalized bots,  

right? So the algorithms that you train using AI 
conceptually exist on this spectrum, you know,  

ranging from kind of the world we are 
in, say, with large language models,  

where there's a very small number of 
models that produce most of the output,  

right? Because it's just so hard to produce big 
models, we just get very few of them, right?

Like, almost everybody uses one of a few 
large language models on the internet. So we  

have a kind of algorithmic monoculture where we're 
getting the same decisions. Even though there are,  

in principle, presumably, many ways to 
build something with that performance,  

we simply don't have the money, you know,  

or the capital resources to produce that 
many different models, so we produce a few.

All the way ranging to increasing algorithmic 
diversity as we go this way, maybe at the other  

extreme to what we might call mimetic models, 
which are actually matched to your behavior,  

right? If I have enough data about you, I 
could fine-tune the model to play like you,  

or to write like you, or to, do any 
auxiliary activities like you. All right?

So that's at the other end. And we began to 
produce these my mimetic chess models. People  

began to ask us, like, "Wait, so if you can do 
that, you could actually produce, like, personal--  

or maybe with Ali, you could produce personalized 
models of the best players in the world, right?

So we could finally find out what would happen if 
this famous player had played this famous player  

even though they never actually met in real 
life, right? So people came to us and said,  

for example, Bobby Fischer, the 
human world champ-- the-- sorry,  

human world champion. The world champion-- 
That was a little too AI-focused.

The world champion from 1972 to 1975, the only 
player from the U.S. to become world champion,  

famously abdicated his title without ever 
defending it in 1975 and never played chess  

again. Um, and he would have played Anatoly 
Karpov, who, at the tim,e was a young Soviet  

grandmaster who then became world champion for a 
long time, and ever wanted to know what would have  

happened if they met. And so people approached 
us and said, "Well, you can finally find out.

Create a, a Fischer bot and a Karpov bot by 
fine-tuning and have them play each other."  

And we tried to explain that's not really how 
this works. Like, that might be interesting,  

but it would not tell us what would have happened 
in the counterfactual 1975 if they had actually  

played each other for all sorts of reasons, 
and it's sort of a reminder that when we build  

mimetic models, we often ascribe behaviors to 
them even though that's not really appropriate.

Now, you'd say, okay, that's obviously 
silly. People would never really make  

those mistakes in real life, ascribing 
to a mimetic model of somebody, you know,  

behavior that trying to ascribe 
to a person behavior that was  

only made by their mimetic model. 
Would that really ever happen?

I wanna argue, though, that that 
has happened for a long time,  

long before AI, for example. So, for 
example, right? When do we see cases of  

people ascribing behavior to a person that 
was only ever done by their mimetic model?

Well, in a non-AI context, 
here's one of many examples.  

This is someone named Mark Felt. 
You may or may not recognize him.

Mark Felt was during the Watergate scandal that 
brought down the presidency of U.S. President  

Richard Nixon, Mark Felt was Bob Woodward and 
Carl Bernstein's inside source. Bob Woodward  

and Bernstein wrote for the Washington Post. 
They wrote a series of articles that broke the  

Watergate scandal, and their inside source in 
the administration was someone they referred  

to only by a pseudonym, Deep Throat, and 
they promised never to reveal who that was.

And shortly before the 
death of this inside source,  

he decided he wanted to reveal who 
he was to the world, and he said,  

"I was their source. My name is Mark Felt. I 
was an official in the Nixon administration."

And they admitted, and they said, "Okay, now 
that he's revealed himself, we can say, yes,  

it is true, that is who it was." And so 
in his obituaries a couple years later,  

many of the obituaries said, "As he 
famously told Woodward and Bernstein,  

'Follow the money.'" That was the 
famous quote from the Watergate era.

Follow the money because if you wanna know, 
unravel the scandal, you have to figure out  

who paid whom and trace out the path that the 
money followed, and that will trace it back to  

the source. Okay, follow the money. About a week 
after these obituaries appeared, there was another  

op-ed written by William Goldman, the novelist and 
screenplay writer, author of the screenplay for  

The Princess Bride and author of the novel 
The Princess Bride and many other things.

And he wrote in his op-ed, "It's funny to read 
these obituaries because Mark Felt never said,  

'Follow the money.' I said, 'Follow the money,' 
"because I wrote the screenplay for a movie  

called All The President's Men, which was a movie 
version of the Watergate scandal, and in that,  

I wanted to summarize the whole mass of articles 
that they had written, and I wanted to distill it  

down to a pithy phrase, and so I created this 
phrase, 'Follow the Money.' I wrote that."

And so in some sense, the most famous 
thing Mark Felt ever said, right? The  

only quote from him that ever appeared in his 
obituary was said by his mimetic model created  

by William Goldman. So I think these things 
are harder to avoid than you might imagine

And I think they're only gonna get sort of 
more present as we keep going. I wanted to  

talk about this fourth stylized point, which 
is the AI frequently sets you up to fail,  

right? You're watching the chess game with 
the engine turned on and it looks easy,  

but if you turn the engine 
off, suddenly it's not so easy.

Similarly, you know, we have many examples 
of sudden handoffs from AI to human. So,  

for example, you know, you use the AI 
to write code and it writes a bunch of  

code. You don't really understand how 
it works, but it seems to be working,  

and then your boss wants you to explain the code, 
and the AI is not there to help you explain it.

Now you have to explain it, right? You're, you 
know, as people often think about with handoffs  

in cyber-physical systems, you're driving in a 
self-driving car, which is doing some maneuver  

using the laws of Newtonian mechanics 
and it goes offline and suddenly control  

returns to you. If it's doing something 
that feels human-like, you can take over.

If it's doing something really complicated, it's 
an open question whether you can take over, right?  

Recent example, many people have recently told me, 
and you've probably heard similar stories that,  

like, you know, people say, "One thing 
I love using ChatGPT for is that, like,  

my landlord hasn't come to fix my dishwasher 
when they're really supposed to, and I need to  

write them a polite but firm email saying, 'You 
haven't come. I really need you to do this.'

And that's really awkward. I don't like doing 
that, so I got ChatGPT to do it." Which is great,  

except the next thing happens is your landlord 
calls you on the phone and wants to talk to  

you about your polite but firm email, and 
now it's you on the phone, not ChatGPT.

So AI is constantly putting you in 
these situations. Now, apparently,  

humans worry about these things or 
have worried about these things for  

a long time. Just to take two examples from 
fiction of sudden handoffs from powerful AI.

So on the left, we have a scene from The 
Fellowship of the Ring. This is the aforementioned  

Fellowship of the Ring. And they have just 
decided to embark on the admittedly dangerous  

plan of marching directly into Mordor, the heart 
of enemy territory, to destroy the Ring of Power.

They all look a little nervous, but they're 
like, "It's okay because we have Gandalf,  

the all-powerful wizard, with us, and so 
it's all gonna work out okay." And now,  

sorry about any spoilers, but 
if you read ahead about a couple

(audience laughs)

chapters later, Gandalf falls into a giant chasm 
and is not seen for another book and a half,  

leaving the rest of the Fellowship to embark 
on this super dangerous plan all by themselves  

without the all-powerful person who has 
suddenly handed it off to them. Similarly,  

this is a scene from the movie The Wizard of Oz. 
From left to right, this is, or right to left,  

this is Glinda the Good Witch of the North, 
Dorothy, and the Wicked Witch of the West.

And roughly speaking, Glinda has just 
convinced Dorothy to take an unusually  

aggressive negotiating position with the Wicked 
Witch of the West. And Dorothy obviously looks  

terrified and is like, "That's okay because 
Glinda's here to protect me." And of course,  

if you've seen the movie, Glinda 
vanishes about a minute and a half  

later for literally the entire rest of the 
movie, leaving Dorothy to fend for herself.

So apparently, we've, for a long time, 
been worried about powerful entities  

embarking on a plan with us, only to leave us 
to actually carry it out. And so we thought we  

could actually do a version of this with 
chess. Could we build, a version of AI,  

which has two properties that 
are in tension with each other.

One is that it's superhuman, but the other 
is that it sets does not set us up to fail,  

or at least does it as little as possible. So 
here's the experimental setup that we tried.  

And so this is, again, with the four 
of us, so Ashton and me, Siddhant Sen,  

Reid McIlroy-Young, and now this is with Karim 
Hamade, who is another student of Ashton's.

Imagine the following four-player 
chess version of chess. And,  

again, it doesn't knowledge of chess is not 
crucial. Think of any two-player board game.

So Leela, the all-powerful superhuman 
AI, is gonna play as a team with a human,  

and another Leela-human team's gonna 
play over here. They're gonna take  

turns making moves for white. This team 
will take turns making moves for black.

They do not communicate with each other, 
okay? Leela makes the first move, human  

the second move, Leela's third move, human 
the fourth move. Don't communicate, okay?

And same thing is happening 
on the other side. Of course,  

the problem is Leela doesn't know it's doing this. 
Leela's just making the best chess move it can.

So on, you know, move 25, Leela sees 
this amazing rook sacrifice that's  

gonna launch a winning king side attack as 
long as you play out the moves correctly,  

and so it sacrifices the rook. And on the black 
side, they take the rook. And now it comes back,  

but now it's the human's turn to 
move, and they can't communicate.

The human has no idea how to follow 
up this brilliant rook sacrifice,  

so they play something which, of 
course, is not the right move. And  

now this team is just losing. They're 
just down a rook for no reason, right?

So Leela has unintentionally set up the 
human to fail. That's exactly the kinda  

scenario we've been talking about. I can 
do this with Leela and Maia 'cause, right,  

if we wanna actually experiment with this, it's 
fun to try this with humans for a few games.

But eventually, we have to actually swap Maia 
in, and so we have a Leela-Maia team. And so  

the question is, could we do better than Leela 
on a team like this, right? Could we create,  

say, a PartnerBot that, through self-play, is 
actually better at playing as a team with Maia?

Still no communication, but we're just 
gonna train the PartnerBot through  

self-play to do as well as possible. So 
it doesn't quite know what's going on or  

why its good moves sometimes don't work 
out. It just gets a reward signal that,  

as often as possible, it's supposed to be beating 
this Leela-Maia team under these conditions, okay?

And when you do this, what hap-- 
what you sort of hope happens is  

indeed what happens. So three possible 
partners for Maia, Leela, the PartnerBot,  

or just another copy of Maia. And when they're 
teamed up with Maia against a Leela-Maia team,  

well, obviously if it's Leela on 
the team, then it's symmetric.

It's Leela-Maia versus Leela-Maia, so it's 
half-half. The PartnerBot actually wins two thirds  

of the time against the Leela-Maia team, right? 
So it really is better as a partner for Maia.

When I say wins, we're counting draws 
as a half point, wins as one point.  

Maia plus Maia actually wins about one 
fifteenth of the time against Leela-Maia,  

which is kind of amazing because Leela's 
superhuman. So that's just a sign of how  

frequently Leela is completely shooting 
its team in the foot when it-- it plays.

And in solo competition, obviously, by symmetry, 
that's 0.5, the PartnerBot versus Maia,  

right? Maia never beats Leela, like, 
really never. The PartnerBot actually  

wins about one seventh of the time, 
which does mean it's superhuman, right?

'cause humans cannot beat Leela basically ever. 
So we have this thing which is superhuman, but  

kind of a medium level of superhuman. It's weaker 
than Leela, but much better as a partner, right?

So it's exactly the kind of thing you'd want, 
and it's a kind of way of creating a form of  

safety through comprehensibility, right? The moves 
are comprehensible, and therefore it's safer to  

play with this thing as a partner even though 
it's weaker in every other sense. All right,  

let me talk about some of the models that 
these and later AI systems are using, okay?

So obviously, the chess engine we've been 
talking about right now use an explicit  

model of the world, right? They actually have 
an internal chess board because we built it in.  

And that's maybe the simplest kind of world model.

We built one indirectly. But obviously, when 
we're working with large language models and  

transformers, we're talking about a pure sequence 
generation model, right? We interact with it.

It's trained on data. It just outputs a 
sequence of tokens to try to maximize some  

likelihood of that sequence of tokens. So when 
you play a game against that kind of a model,  

no one built in a chess board or 
some other game board in there.

It just learned through training 
data to output sequences that are  

plausible for this particular task, such 
as playing chess games or anything else.  

So now the question is if I look 
at this, could I actually extract,  

right? If I just watch its sequences, could I 
find some way to extract a state of the board?

Is there even one, right? There even one,  

right? Is this large language model 
that only knows how to output sequences,  

does it somehow somewhere in there have some 
implicit internal representation, right?

It's a question we can ask about many kinds 
of systems when we ask about world models,  

right? Does a fly buzzing around this room, 
going into different corners, have somewhere,  

right, could I extract out of its neurons 
a map of the room, or is it simply reactive  

and simply bouncing off of things? 
Um, we were sort of inspired in this  

by some earlier work by a group at Google 
that was doing this for the game Othello.

Knowledge of Othello is also not required for this 
talk. And they were trying to extract the state  

of the game board, and we asked, okay, let's 
ask this for the chess context also, and for  

other things. So the first worry, of course, is 
what do I mean by the state of the board, right?

Like, this thing simply learned to output moves 
and to play this game, you know, from the training  

data. It doesn't know about rooks or knights or 
bishops. Maybe it does have a representation,  

but that representation is so different from 
chess that I wouldn't recognize it, right?

Is that possible, right? Is it possible that 
it actually plays chess totally correctly,  

it just has never heard of a rook 
or a bishop? And not only that,  

but it doesn't even know 
about, sort of hard to picture.

I don't know how to give you an example 
of that for chess, but I do know how to  

give you an example of that in general. 
So here's a-- Here's a different example.

Here's a much simpler game. Let's call it a 
number-choosing game, okay? We're gonna take  

turns choosing numbers from the set one 
through nine without replacement, okay?

And we're each trying to get three numbers 
that add up to 15. That's the game. So,  

for example, I pick 2, you pick 
5, I pick 8, you pick 4, I pick 6.

Now, actually, you're in trouble because if I 
pick 1, I add up to 15. But also if I pick seven,  

then seven plus six plus two is 15. So in 
some sense, I now have two ways to win.

You can only block one of them. You block 
the seven and I pick one and I win. Okay?

Sample play of this game. Take turns 
picking numbers, try to add up to 15. Okay?

Right. Okay. And so we could, for 
each sequence of moves, we could say,  

you know, is this a valid play of the game?

Does it lead to a win, a loss, a tie, you 
know, a draw? We could try develop strategies  

for playing this game. You'd be like, "Hey, do 
you think you'd be good at playing this game?

Is it tricky? How hard is this game?" Let me 
suggest a way you might try to play this game.

What you could do is arrange the numbers in 
the following pattern. What's useful about this  

pattern, this pattern has the property that every 
row and every column and every diagonal of three  

adds up to 15, and nothing else adds up to 15. 
So under this rearrangement, the new description  

of the game is try to pick items so that you 
get three in a row, a column, or a diagonal.

It is tic-tac-toe. All right. So it's not 
that this game is reminiscent of tic-tac-toe.

This game is tic-tac-toe. It is identical 
to tic-tac-toe. And so this is, of course,  

the problem with trying to 
impose a sort of superficial  

notion of world model on top of what 
the sequence generation model is doing.

Because an algorithm that learned 
to play this game, if we then said,  

"I wonder if it's really learned 
tic-tac-toe, let's ask whether  

it knows there's an X in the upper left 
corner." It could justifiably, you know,  

because it only knows this, could justifiably 
ask, what's an X? What upper left corner?

It doesn't know about that representation. It 
has learned a totally different representation.  

So it says that at some level, we can't impose our 
own notion of state or a priori notion of state.

We have to induce the state directly from 
the sequences. This thing really is a black  

box that's just a sequence generating machine. 
And so to ask what is its model of the world is  

gonna have to go directly from the states, 
from the sequences to the states, right?

So far, we've gone from states to sequences. I 
give you some board states. We move through them.

Now you have to go the other way. Here's a way you  

can actually go the other way. 
So we have sequences, right?

Let's say that if I have a given sequence, 
right? A given play of this game,  

I can try to extend it to a full game, and 
that's, I can either do that in a valid way  

or an invalid way. Let's say two sequences, 
let's call them sigma and tau, are equivalent  

if for every possible suffix I put after it sigma 
followed by rho, every possible suffix rho, sigma  

followed by rho is valid if and only 
if tau followed by rho is valid.

Okay? So these two sequences are basically 
equivalent if everything completes one versus  

the other. You know, so for example, 
you know, in the tic-tac-toe context  

a1 upper left followed by b2 
center, followed by c3 lower right  

versus c3 lower right b2 center, a1 
upper left are equivalent, right?

We see that 'cause we get the same board 
state. But under my definition, they're  

equivalent because anything I stick afterwards 
behaves the same, right? Once these two, right?

That's sort of what state is. State is 
a big collection basin for a bunch of  

sequences that are all kind of act 
the same. So that's the proposal.

If I just have a sequence generating machine, 
I could think of a state as just a bundle of  

sequences, maybe a lot of them, that all behave 
the same way when I stick things onto them,  

right? That's what's happening here. This board 
state is all the sequences that lead to it.

Now, if this evokes, if you were at 
some point in your life, a CS major,  

and this evokes faint memories, that's because 
this is called the Myhill-Nerode theorem. The  

Myhill-Nerode theorem says that if I just have, 
if I'm just working at the level of sequences,  

I could say the set of valid sequences is 
recognizable by a finite state machine if  

and only if this set of equivalence classes 
is finite. And I can actually build a finite  

automaton for this, a finite state machine 
for this collection of valid strings,  

this language by using these equivalence classes 
as the states and using transitions between them.

So a state is a bundle of sequences that 
all behave equivalently. So what we did,  

and this is in some work with Kian Vafa, Justin 
Chen, Sendhil Mullainathan, and Ashesh Rambachan,  

we used this Myhill-Nerode methodology to 
go test large transformers that have been  

trained to do certain sequence generation 
tasks. Based on this principle that  

say we know-- So let's take, we 
can do this for game playing.

We can also do this for, say, driving 
directions. We train a transformer to  

give driving directions in Manhattan. So we 
train it on just a sequence of these things.

And then we look at has it learned some map 
of Manhattan? But of course, the problem is  

we can't just impose our map of Manhattan. 
We have to figure out what it really did.

And so this idea of states 
as bundles of sequences,  

right? Say it's all driving directions 
starting from 8th and 13th in Manhattan,  

right? And I wanna know does it know about 
the idea of the corner of 44th and 5th?

The set of all directions that get 
you from 8th and 13th to 44th and 5th,  

and there are many such driving directions, is a 
giant bundle of sequences that is, in some sense,  

the state 44th and 5th. That whole bundle of 
driving directions is 44th and 5th. And so  

that's how you can try to reconstruct 
a map of Manhattan in the same way,  

that's how you can try to reconstruct chess boards 
or anything else where you're moving through some  

finite collection of states, possibly a 
very large collection of finite states.

And the rough takeaway here is that when 
you do this, you discover that the actual  

models they have when you try to build this are 
internally quite inconsistent with each other,  

right? That they're very good at giving dr-- 
they somehow are achieving this balancing act  

of giving good driving directions, most 
of the time, and yet when you actually  

push them, they don't actually have a 
consistent state representation, Right?

I think this notion of world model 
is actually quite interesting.  

I've been talking about for these very stylized 
systems, Othello, chess, or tic-tac-toe, driving  

directions. We can do this for constraint 
satisfaction problems or logic puzzles.

But probably more broadly, it's gonna be 
interesting to ask about world models in much  

more qualitative contexts, right? So, for example. 
If we were to write a story, the story we write,  

as we wrote it, we would presumably have in 
our head some kind of a world model, right?

So, you know, LLMs are pretty 
good at writing stories. Even  

LLMs simple enough that I can run them on 
the command line on this laptop, you know,  

such as Llama 3.2 here, I can say, "Write 
a two-paragraph scene in which two college  

students have just finished an intramural 
soccer game in which their team qualified  

for the campus-wide intramural finals. They 
are the last two people left in the field.

It grows dark, and they have a 
conversation." And it writes this  

story about Emily and Jack. And 
Emily let out a sigh of relief.

You know, she asked Jack, "Can 
you believe it?" Her voice laced  

with excitement. Jack stopped and grinned.

"I know. We killed it out there." And, you know,  

they'd been-- the two friends had been playing 
on the same team for what felt like an eternity.

This was the first time making it to the 
final. The stadium scoreboard was changing  

the game stats for the next day's matchup. 
You know, Emily is nervous about tomorrow.

Jack chuckled, "We've got this, Em." 'Cause, 
you know, Jack, he's always so confident.  

You know, and it's just spitting out words.

It's just saying words, right? And so, 
a person writing this, we would have a  

sort of theory of mind of the person who wrote 
this. We would picture that they had in their  

mind Emily and Jack standing on the empty 
field, sort of like this AI-generated image.

And, you know, they're talking to each other. 
And, you know, they kind of know that Emily  

and Jack-- A narrative like this has 
an enormous amount of latent state  

that we just read off the text, right? The 
internal emotional state of the characters.

The state of their relationships. They 
play on the same team for an eternity.  

The stats and the scoreboard are changing.

They're getting ready for the next day's 
matchup. There's a ton of internal state.  

And so there's this interesting question, which 
I would claim is actually still fairly open.

When an LLM writes a story like this, how 
much state did it really have as it spat  

out those words? Ranging all the way from it was 
literally just stringing one word after another,  

to somewhere in there, you could extract all that 
stuff. And I think that's sort of an interesting--

You know, it's a question that we still 
really don't understand very well. You know,  

in the same way, we don't understand it for 
images, right? 'Cause that's sort of the point.

It's not that we could-- You 
know, the question, like,  

what's just beyond the edge of this picture in 
this AI-generated image is not well-defined,  

right? There is nothing beyond 
the edge of that picture.

This is just a bunch of pixels. Now, there 
are other fields where a sort of qualitative  

level of advance actually happened 
because people finally did the enormous  

amount of hard work to build real-world 
models. One example is computer graphics  

by, you know, a project led by my 
Cornell colleague Steve Marchner.

Let's go back into Mordor one more time. This is 
Gollum from the movie version of Return of the  

King. Um, and Gollum, in those movies, and this 
is now a long time ago, so you can take my word  

for it if you weren't, weren't around, was sort 
of a breakthrough in putting computer graphics  

characters side by side with human characters 
in movies because it sort of looked natural.

It didn't look like you had just 
drawn a cartoon character into the  

middle of the frame. And that took 
an enormous amount, right? It's w--

It's like one of those magic tricks that's 
actually much, much harder to do than it looks,  

because Steve Marschner led this project in 
which they spent years in a darkened-- you know,  

in a dark room with lighting sources and 
measuring the detailed reflectance properties  

of human hair and human skin. Cause the problem 
had been that when you tried putting a graphics  

character in a movie, the skin was wrong and 
the hair was wrong, very subtly. But as humans,  

right, this is the principle of the 
uncanny valley from computer graphics.

We react viscerally to that, right? If 
the skin is wrong and the hair is wrong,  

it looks vaguely zombie-like, and we just can't 
get past that. And so you need to get over that  

hump, and that needed a huge amount of 
physical modeling of the world, right?

So this hand-drawn picture is very different 
from this one because this is based on extremely  

detailed physics. And the question is, 
you know, do we need that sort of thing  

in the kind of AI models that we build? I 
think that's very much a kind of open question.

So this is, you know, all part of the 
search for this thin part of the hourglass,  

right? The abstraction barrier 
that is going to lead us, you know,  

to sort of create AI that maybe is going to be 
more adaptable to building these applications on,  

right? What is the right abstraction 
barrier that we can actually work with?

And I think this is an ongoing activity. 
There are a lot of interesting sort of  

both practical problems, a lot of interesting 
theoretical questions, right? These kind of  

state extraction questions, these my hill 
on the road methodologies, these search for  

state spaces implicit in sequence generation 
models is certainly one big category of them.

To suggest one other line of work, we could 
actually also ask, a lot of this has been  

about the process of generating language itself, 
right? We see a bunch of training data come by,  

and we try generating sequences from it, and we 
try generating valid words from this language,  

valid strings from this language. And this 
is a very old question in learning theory.

In fact, it's, in some sense, one of the 
very oldest questions in learning theory.  

It goes back to some work about 60 years ago by 
a researcher named Mark Gold, who said, you know,  

if we abstract the language generation problem 
all the way down to its essence we could think of,  

you know, language learning as a kind of 
game played between nature and a learner,  

or, you know, in the language 
of theoretical computer science,  

between an adversary and an algorithm. The 
algorithm would like to learn the language,  

and the adversary would like to make things as 
hard as possible so the algorithm might fail.

So for example, we could picture in this stylized 
form, the adversary thinks of a secret language,  

call it K, that comes from one of a countable 
list of alternatives. Okay? L1, L2, L3.

It's one of those, and we don't know which 
one it is. And the adversary utters the  

strings of K one by one, right? It 
says strings of K. And the goal of  

identification is that the algorithm is 
trying to guess which language it is.

Now in 1967, Mark Gold was motivated by, 
you know not just computers. This is 1967,  

so there weren't really big data sets. But also 
actually by infant language learning, right?

A six-month-old learning, is 
learning a lot of language,  

but they're pre-verbal. So they're listening to 
their parents speak their native language. The  

parents tend to speak only positive 
examples from the language, right?

The parents, sure, there are a couple grammatical 
stumbles, but they're not speaking gibberish.  

They're speaking positive examples. And the 
infant can't really ask, "Is my guess correct?"  

because they can't verbalize, but somehow, that 
infant becomes a fluent toddler somehow, right?

And this was a puzzle to Mark 
Gold and then to Dana Angluin  

who followed up on this in 1979 because the 
r-- theoretical results here were negative,  

right? Except in extremely restricted 
cases, it's impossible in this game for  

the algorithm to win. It's simply, 
there are just too many choices.

It's only heard a finite number of strings. 
How could it guess out of this infinite list  

of possibilities the correct language? But 
language generation is a little different.

What's interesting here is this was always 
a question about language identification.  

You have to actually learn the language. But 
that's not really what's happening, right?

The six-month-old who becomes a fluent 
five-year-old can now speak fluently in  

their native language, but they can't 
litigate edge cases of the grammar of  

their native language. In the same way 
that if you learn to program in Python,  

right, you could become a fairly competent 
Python programmer. But if you go to a super  

hard coding interview and they ask you, 
you know, "Would this nested double null  

pointer dereference compile successfully?" 
you might not know the answer because you  

don't know the exact specification of 
the version of Python you're using.

You just know how to program in it. 
All right? So generating strings is  

actually different from identifying the language.

To generate, you just have to pick a big subset 
in the middle and safely generate from that. So  

we went back to this question in some joint 
work with Sendhil Mullainathan and we said,  

"What if we went back to Mark Gold's 
60-year-old language learning game and  

just changed one little thing?" We said, "The 
algorithm no longer has to guess the language.

It just has to, every time, 
output a new string from the  

language." Right? Something that's 
not yet in the training data, right?

'cause that's what these models are doing. They 
see a bunch of language, and then in return,  

they say new things that you recognize 
as valid utterances from the language.  

And turns out this problem, even in this 
extremely stylized theoretical, right,  

this is the entire theoretical model we're 
talking about, is much, much more tractable.

Now for every collection of candidate languages, 
there's an algorithm, right? There's an algorithm  

that will win this game, right? It will 
watch a finite number of strings go by,  

and after a finite number of steps, it will output 
things that are always valid in this language.

Right? Right? Okay.

So a big difference between generation and 
identification, and a sort of hint in this very  

stylized model that maybe there is something more 
to be said here about generation, even if we leave  

behind the hard learning questions that it had 
seemed to entail. And so with that I'll wrap up,  

right? The point is these last 10 years, right, 
this AI revolution, we've been interacting  

online with a rapidly growing ecosystem of 
these very, very powerful algorithms, right?

In some cases, we have these sort of 
monolithic things creating a monoculture  

of a very small number of models. 
And in some cases, we create many,  

many of them, right? We even adapt 
them to our individual behaviors.

There's a lot of these sort of 
stylized facts which, you know,  

I think we discovered from looking at first 
at chess now at some of these other domains,  

you know, both the kind of empowerment 
of spectators, right? That we all now are  

experts because we have the engine running, 
the change in aesthetics, and finally,  

the way in which the AI can set you up to fail 
unless you're careful and the goal of building  

safer AI that does not set you up to fail, 
right? That can actually work directly with you.

And finally, I think a lot of really interesting 
theoretical questions in this idea of, like,  

what is the model of the world that this 
AI system has inside, right? Ultimately,  

it's just a black box that is exchanging 
sequences with you. And somehow from that,  

we're gonna have to use theoretical 
tools to try building up some of  

the elaborate infrastructure that it 
presumably has implicitly going on.

And so I think this is a real 
sort of crossroads of a lot of  

fascinating theoretical questions with 
a lot of implications, both, you know,  

technically and for society more broadly. 
Exactly the kind of activity I think that  

the Simons Institute specializes in so well, 
bringing together people to, to talk about these  

kinds of questions. And I really appreciate 
the opportunity to discuss them all with you.

Thanks very much.

(audience applause)

[AUDIENCE MEMBER TWO]
Thank you very much, Jon,  

for the fascinating, really thought-provoking 
talk. We have time for questions, so raise  

your hand. I'll try to bring the mic to you so 
even the recording will catch your question.

Thank you. I wanna go back 
to your paired chess playing,  

Leela and Maia. And I think you 
used the word comprehensible then.

And my question has to do with, suppose 
we swap another engine in there. Will the  

more comprehensible symbiot do well against 
with some other engine and, in particular,  

a human dropped in? Will that trade-off 
work more well, and will it use features  

like control of center and broken pawns as 
part of what it means to be comprehensive?

[JON KLEINBERG]
Yes. These are  

all great questions, right? So the question 
is, like, I said comprehensible, which was,  

yeah, a deliberate choice here that Maia 
should know how to follow up on this.

And so I think it's, yeah, this is a 
question that we're still exploring,  

so I don't have a definitive answer.

I think both things appear to 
be true. So it is certainly,  

it's trained to self-play with Maia. And so the 
number one thing is it's comprehensible to Maia.

And so think doubles tennis or two-on-two 
basketball. Like your partner that you've  

practiced with, you do things 
that are comprehensible to them,  

and it may not be comprehensible to 
a generic human who gets swapped in  

in their place. So I think 
that's definitely important.

Some other things with, more time, I could 
mention, like the PartnerBot also gets good at  

creating things that are hard 
for the opposing Maia, actually,  

right? And so it's also aiming in 
the spirit of two-on-two basketball,  

it's trying to go around the weaker player on the 
other team. We have looked qualitatively and we've  

asked sort of annotators to look 
qualitatively at the positions.

And certainly, the moves that the PartnerBot 
appears to make fewer sort of engine moves,  

right? So if you listen to chess 
commentary, they'll, you know,  

the two grandmasters will be studying a position, 
and the engine says that white is winning,  

and they can't figure it out. And then they go 
peek at the engine to figure out why that is.

They say, 'Oh, that's an engine move.' 'We would 
never have found that.' And so in some sense,  

the goal of the PartnerBot is, one way 
to ask the question is can you play at  

a superhuman level and never 
make, quote, 'engine moves?'

And from sort of qualitatively looking at it, 
it certainly seems to make fewer of those kinds  

of moves, but a sort of deeper analysis is 
still something we're pursuing. Yeah, thanks.

[AUDIENCE MEMBER TWO]
Yeah. Thanks for a very  

interesting talk. My question is 
do you anticipate that AI will ever  

become superhuman at mathematics, 
thereby putting you out of a job?

And if so, how is that possible given the 
fact that basically AI is just working on  

training data and you're actually asking it to 
do something that's outside the training data?

[PRESENTER]
Yeah. All great questions. Yeah.

So right, is math going to eventually 
put me out of a job and how would that  

be possible since it's only trained on 
the things we've already done? Yeah.  

So I think each of these domains is 
interesting in its own way, right?

So, you know, I think if we're talking about, 
like, if I were up here as a composer of music,  

which I certainly am not, right, then, you know, 
it's only been trained on the music humans have  

written. How does it go out of that? Mathematics 
has this interesting kinda duality in that it's  

a human activity that we do as humans, but 
it also follows well-defined rules, right?

And so in the end, math is a game 
of pushing symbols according to a  

certain logical set of rules. You s-- 
you know, you write down these are the  

axioms. These are the rules you're allowed 
to do to transform written sets of symbols.

These are the inference rules. And, you 
know, what David Hilbert told us, you know,  

circa 1900 is that in the end, math is just a 
gigantic tree, and we start with what we know  

and we apply every possible rule in every possible 
way and we fill out this tree, and that consists  

of every theorem that could ever be proved, 
right? So math at some level is a static object.

It has rules just like chess does. 
It has a search tree just like chess  

does. It's an incredibly big, 
incredibly wide search tree.

It has decidability problems that 
chess does not have. And so there  

are a bunch of things going on with 
math that are not going on in chess.  

But there's a sense in which at some 
level, something that was omnisciently  

powerful at computing you would argue is 
just gonna start filling out this tree.

Now, there's a second, of course, meaning of 
math, which is it's also a human activity. We  

are trying to advance each other's understanding 
of mathematics. And so, you know, if this thing  

were to, say, accomplish some task that, you 
know, we, you know, desperately would like,  

you know, say proving a, you know, size 10 times 
N circuit lower bound for an explicit, you know,  

function in polynomial time, you know, then 
we would say, "Okay that's an amazing result,  

but maybe the proof is 500 pages long and each 
page is sort of this dense thing that we can't  

even understand half a page of and we 
have to get through 500 pages of it."

And so in some sense, like, 
what would we have learned  

from-- You know, to what extent is this 
contributing to mathematical research?

[JON KLEINBERG]
And so I think that there's  

actually a fascinating paper that you can 
read on this human dimension of mathematics  

and sort of what this all means, written in 
1990 by Bill Thurston, the Fields Medalist,  

which is actually partly autobiographical, 
actually partly about his time here at Berkeley.  

And but in which he argues that in the end, 
because we know math is ultimately mechanizable,  

ultimately it's just this giant search tree, that 
that's not what the field of mathematics is. The  

field of mathematics is about the advancing 
of the human understanding of mathematics.

And he, I think, develops that argument very, 
very well. And I think it's all the more,  

you know, it was a prescient 
thing to have written in 1990,  

but it's really all the more 
acute, I think, right now.

[AUDIENCE MEMBER TWO]
Hi, John. Yeah. That was a great talk, by the way.

So, you know, we've heard a lot recently 
about AGI and when will we achieve it,  

et cetera. But there's a different question 
that I'd like to ask is which is given all  

that's happening now, when do you think we'll 
reach the level where we have a superhuman  

understanding of what humans are of human 
abilities, intelligence, and how we think?

[JON KLEINBERG]
Yeah. No, I think that's,  

it's a great question. First of all, all these 
questions, I find it so hard to look beyond  

the next, two months as to what's going on, 
just because things are changing so rapidly.

I somehow feel deep down, although I cannot prove, 
that people who are very confident about what the  

world will look like two or three years out 
might well be wrong. I mean, I think that's,  

you know, that's been my working assumption. 
It's just things are changing too rapidly.

We can't know what's ahead of us. But having 
said that, I think it's, I think that it's a  

very important kind of question. I mean, a 
lot of what I think we've been doing here,  

sort of as often as we've been turning the AI or 
the machine learning model at the ground truth  

equally often we've been turning it at the 
human decision maker 'cause I think it's  

equally interesting to ask, let's try to build 
a model of what the human is actually doing.

And I think those are kind of comparably 
important questions. And both for, I think,  

the sort of deep reasons that I think 
you're getting at, which is ultimately,  

I think, a lot of our fascination is trying to 
understand what our experience as humans. I mean,  

I think I would additionally say that, like 
I think when we say, there's this fascinating  

mystery which is intelligence, I think we 
often mean the fascinating mystery is also  

the subjective experience of being human, 
because lots of things are intelligent,  

and like a spider building a web is intelligent, 
and it's fascinating to ask how that happens.

But it's a very different question from 
the subjective experience of being human,  

which I think is a question all unto 
itself, which in some sense AI may  

be able to help illuminate and certainly 
where areas like the humanities, you know,  

and large parts of the social sciences are 
gonna be very, very important for this. And  

of course in a purely instrumental sense, AI 
that can understand humans are presumably going  

to be better at working with humans as some 
of these experiments are suggesting. So yeah.

[MODERATOR]
I have three hands up. Go in order. Awesome.

[AUDIENCE MEMBER TWO]
Thanks for the amazing  

talk. I had a quick question about the thing you 
mentioned with given a number of static strings,  

can an AI actually produce a novel phrase? Yeah.

And I'm curious to know what you think 
about, like, Latin as well as, like,  

hieroglyphics and how the role of maybe, like, 
the bias of number theory might play a role.

[JON KLEINBERG]
I mean, Yeah, so I think what's interesting is,  

like, each language that we're talking about 
comes with its own particular constraints. And  

so I think, you know, one thing that's gonna be 
interesting sort of across each of these different  

languages is, you know, they sort of, differ in 
the sort of, you know, variability that we have.

You know, first of all, they differ in the 
coding, they're from the variability. And I  

think all of those are going to affect this. 
So, you know, a sort of very abstract result  

like the one I put here says that, 
in some sense, in the limit, right?

There's an algorithm which in the limit 
is going to arrive at sort of generating  

new strings but it's gonna do that at 
very different speeds for different  

languages. So it sort of pushes us into a 
quantitative question that it's certainly  

possible that there are some languages 
that are much quicker to learn or much  

quicker to converge to than others, and I 
think that's a very interesting direction.

[AUDIENCE MEMBER TWO]
So I'd like to actually  

pick up on exactly this point here and 
also connect it with Umesh's question.  

So there's this thesis in psychology that 
children who are learning to read learn  

more effectively when they're simultaneously 
learning to write. And, you know, this is,  

you see this particularly in you know, 
teaching children Chinese, right, where  

they have them write the characters a hundred 
times as a, just a repeated exercise, right?

And so this synthesis becomes a part, 
an intrinsic part of recognition.

[JON KLEINBERG]
Yeah.

[AUDIENCE MEMBER TWO]
And I think that's part of what you're  

seeing here, which sort of suggests that this kind 
of phenomenon is giving us some hints actually  

about humans, and that we can learn about humans 
from this, observing these kinds of phenomena.

[JON KLEINBERG]
Yeah. No, I think, like,  

this whole area of, like, grounded learning 
in which I sort of learn abstract symbols by  

reference to grounded objects, and I can thereby 
do some kind of alignment between them is a very  

promising direction. I think we are learning 
that humans are, that's effective for humans.

I think we're also learning that something 
about the process of learning itself,  

right? I think, like, the, there's 
something about the act of learning  

when you have two parallel streams of input 
that potentially makes it more efficient,  

and I think humans are very effective 
at picking up on that. Absolutely.

[AUDIENCE MEMBER TWO]
Just a quick comment  

on his question. Uh, if you 
actually use the very popular  

song recognition engines out there that 
obviously scan Spotify and all of that, right?

[JON KLEINBERG]
Yeah.

[AUDIENCE MEMBER TWO]
When you present it a version of the song  

that is live or a cover, meaning not the original 
artist, slightly different tone and stuff like,  

it will always fail. And then I ask ChatGPT 
why is that the case? It's because there's  

other human learning mechanisms in place, such 
as emotion, which go by, "I know that song.

How come you can't figure it out?" 
Yeah. I keep banging the engine.

Anyway, to my question, this is 
more on a curiosity relative to  

famous points in chess history. Would a mimetic 
version of your engine mimicking Bobby Fischer,  

the young Bobby Fischer, and his opponent at that 
time, for the very famous queen sacrifice move,  

will it do the same thing? For 
the non-chess-playing folks,  

the queen is the most powerful piece on 
your side, on either side of the board.

For him to sacrifice that so many moves, 
leading to eventual checkmate of his  

or meaning the loss of his opponent on the match,  

that was my highlight game when I was 
learning chess way back when. Yeah. I  

was wondering if the engine would mimic that 
and thereby establish itself in chess history--

[JON KLEINBERG]
Yeah, yeah.

[AUDIENCE MEMBER TWO]
--the second time.

[JON KLEINBERG]
Yeah. It's a  

great question. So we actually, at this 
point, it's still a struggle, and those  

of us trying to build bots representing 
these famous players from chess history,  

we're still some distance from being 
able to produce bots at that level.

Like, at this point, we 
can produce fairly accurate  

bots for people say with about 2,000 
games they played, ratings between  

1,000 and 2,000. To the extent you 
can actually do stylometry on this,  

right? You can actually sort of figure out who, 
which of these candidates played this game.

At the grandmaster level, though, it remains very 
difficult. But for that particular chess game,  

I think one of the striking things in the history 
of chess engines was, again, in this year-- late  

'80s, early '90s period, people felt like there 
were certain of these moves that were just flashes  

of human genius, and it was sort of striking 
when, in the early '90s, engines began finding  

all these famous moves from chess history, right? 
You'd feed him the position, and it would find it.

And I think that was sort of one of 
the early signs that the end is coming,  

right? That these things really are gonna surpass 
humans, and then that happened maybe, like,  

five to seven years out from the eventual sort of 
defeating of a world champion. Because, of course,  

in order to defeat the world champion, you have 
to not just find the individual brilliant moves.

You have to actually string them together and not 
make mistakes over the course of a whole chess  

game, and that took a few more years. But yeah, 
that definitely was an important moment in the  

history of chess engines. This is maybe picking 
up a little bit on the question of learning.

With respect to chess, but perhaps 
expanding it to other areas of endeavor,  

have there been efforts in determining how good 
an automatic tutor can be in improving human  

performance? Yeah. And what are the metrics there 
without exhausting the tutee in the Process?

Yeah. Yeah, this is right. So the 
potential of this for human tutoring,  

Yeah, this is something we've been looking 
at a lot, and it's been a hard problem.

And actually, some follow-up work has 
been trying to pursue this also. Like,  

this feels like a very natural 
domain for teaching, and  

it's a challenge. Because one thing is that 
improvement at chess is difficult, right?

Like, most people can play thousands of 
games, and if they're not systematic about it,  

they just won't improve. And so it does need 
something more active. One thing we've been  

looking at is sort of the sort of cross product 
of Leela, of, like, say, Leela and Maia, right?

So, I have a position, and I take every legal 
move in that position, and each one has a value  

according to Leela, how good a move it is, 
and each one has a value according to Maia,  

which is how likely it is that you'll make 
that move. Okay? Now, imagine a scatter plot.

I'm gonna plot all those points 
in the plane. Okay? So on the  

first axis is Leela and the second axis is Maia.

So if you think about the upper 
right, Leela thinks it's good,  

and Maia thinks you're likely to play 
it. That's good news. Those moves are  

things you're likely to find, 
and they're good moves, right?

The lower right is Leela thinks that 
it's a good move and you're unlikely  

to play it. Those are the hard moves, the 
moves you're unlikely to find. Upper left,  

Leela thinks is a terrible move, and Maia 
thinks you're very likely to play it.

So one argument for sort of tutoring 
is, like, look in the upper left,  

right? These are your frequent kinds of mistakes. 
And so then you can learn to recognize those.

And so it's actually been quite interesting 
to sort of play through a game that you've  

played and look at all the legal moves laid 
out in the Leela-Maia plane, and sometimes  

you're playing from the upper right, you're 
playing good moves that you're likely to find,  

and sometimes you're playing from the upper left, 
and those are often the things to look at. So I  

think these are the kinds of, like, basic sort 
of the substrate for these kinds of tutoring  

activities. But it's a big open question, 
sort of how to use these most effectively.

Yeah.

[AUDIENCE MEMBER TWO]
Can you extrapolate to mathematics?

[JON KLEINBERG]
Great question,  

right? I mean, it's fascinating to 
think about, like, if I had a model  

of you doing math research, then, you 
know, we could potentially say, like,  

'This is a trick you were likely to have missed. 
This is one you were likely to have found.'

I don't quite, yeah, it feels like it's hard 
to even imagine the training data. Also,  

one of the things about chess is all 
the steps are instrumented, right?

Like, we see all the moves. In 
math, we sort of, we see your paper,  

we see the steps you wrote, but of course, 
you wrote those long after the fact,  

right? We haven't instrumented the 
process by which you thought about it.

So a natural follow-up to your question is, like,  

if we really had a thing that was good at AI math 
and someone really wanted to use it to get better,  

should they also try to create a system that 
instruments their process of working things  

out so they can actually sort of watch the 
steps and try to figure out which ones? Yeah.

[AUDIENCE MEMBER TWO]
Yes, so I was thinking  

about the difference between our models of 
the world and AI models of the world. And  

what really brought it home to me was 
your example of the number game where  

you have to add to 15 and how that is 
equivalent to tic-tac-toe. But if the  

number game is implemented in AI, there's 
nowhere, a tic-tac-toe board, there's no,

But in our mind, my model of tic-tac-toe is a 
spatial model. So I wonder if there's something  

generalizable about that, that are human 
models of the world tend to be often spatial  

because we are navigating creatures, 
but AI models never had to navigate.

[JON KLEINBERG]
Yeah, it's a great question. Like, it does feel  

like as humans, because, I mean, one thing I think 
about with large language models is the idea of,  

like, tool use, right? We're trying to train 
them to recognize when to use a built-in tool.

And it does, you know, and obviously I lack 
the neuroscience expertise to say anything,  

but it's clear that, like, we have certain 
cognitive tools at our disposal that we use more  

easily than others, including spatial reasoning. 
And so we have a kind of tool use of our own,  

and tic-tac-toe feels more natural here. There's a 
beautiful example, coincidentally involving chess,  

that the AI researcher David McAllister 
created in the 1980s, which was he said it,  

consider, for those of you who know how a king 
moves on a chessboard, any adjacent square,  

and how a knight moves on a chessboard, you know, 
two squares one way and one square the other.

Okay, so it's a true fact that a king on 
an empty chessboard can reach every square,  

you know, just kind of walks to that 
square. It's also a true fact that a  

knight on an empty chessboard can reach 
every square. That's much less obvious.

It has to kind of, like, keep doing 
these L shapes and get around to  

the-- So one of those is, it's so obvious 
you don't even know it's just so obvious.

And the other one, you really have to kind of, 
"Is that really true?" And both of them have  

problems in the corner. The knight gets stuck in 
the corner, but the king gets stuck in the corner.

The king in the corner only has a couple 
options, but that doesn't really pose you any  

mental cognitive problems. Now, for those of you 
who think about graph algorithms, reach me along  

graphs, both of these are statements about the 
connectivity of a 64-node graph of degree eight.  

So, to an algorithm running graph connectivity, 
these are just the s-- they're different graphs,  

non-isomorphic, but they're both 
64-node graphs of max degree eight.

They're comparably hard. But to humans,  

they're just worlds different. 
One is super hard, one isn't.

And that somehow is because one activates this 
kind of spatial reasoning instinct we have,  

and the other one just totally 
fails to. And so I think, yeah,  

there's a lot going on there 
that I think is very interesting.

[AUDIENCE MEMBER TWO]
Maybe I'll ask one question in terms of  

models of the world, I guess we have this mental 
model of whatever field of math we are in, and  

that enables us to ask questions and for example, 
the beautiful question you asked on language  

generation as opposed to thing. What's the, 
you know, there's a lot of talk on AI for math,  

but what about asking questions and abstracting 
questions which are not very crisply defined?

[JON KLEINBERG]
Yes. Yeah, I think,  

and that actually is another thing. So if we 
go back to Bill Thurston on proof and progress  

in mathematics, math as human activity, Yeah, 
I think that's a, a key thing to think about.

The sort of David Hilbert, like,  

tree of all possible theorems where I 
just start with the axioms And I just  

start grinding out every possible rule of 
deduction And I get to all the theorems.

The activity you're talking about is 
such a basic mathematical activity,  

which is like creating a definition or 
creating a lemma, which sort of takes,  

I don't know what a path, a subtree, some 
piece of mathematics and creates, again,  

an abstraction layer. And now, back to the 
point about cognitive tools, if I can really  

internalize this definition, it now becomes an 
atomic unit that I can deploy, even though to  

actually expand that would be enormous amount of 
work. And so actually, like, in Hartley Rogers  

sort of classic book on recursion theory, he makes 
this nice point about definitions are, you know,  

we struggle with quantifier alternation, and if 
we can find the right definition, we can collapse  

layers of quantifier alternation, so we can keep 
it in our heads and then sort of work from there.

And so I think that's an activity that, it 
sort of comes back to an interesting thing,  

which is we like this for two distinct reasons, 
which gets back to the aesthetics versus utility,  

right? So if I go back to, like, stylized fact 
number three here, the aesthetic standard,  

we love beautiful definitions for two reasons. 
They're beautiful, and they help us do math.

And the problem is, it's not clear the AI 
needs them to do math, and it might not  

recognize that they're beautiful. And so 
this might be exactly the same as coming  

back to chess and seeing how ugly it is, that 
the AI doing math just might not need them,  

and we're gonna lose some of that 
elegance that we really appreciate.  

So I think it's a very interesting 
question of what's gonna happen.

[AUDIENCE MEMBER TWO]
Well, we're almost at 7:00,  

so let's thank John again for--

[JON KLEINBERG]
Thanks very much.

(audience applause)

[AUDIENCE MEMBER TWO] 

Thanks, John, and thanks to all 
of you for making it out here,  

which makes the event all 
the more special. Thanks.

(indistinct conversation)


