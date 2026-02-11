[JESSICA HULLMAN]
Yeah.

[MODERATOR]
It's not always Simon's.

[JESSICA HULLMAN]
Yeah.

[MODERATOR]
But it's certainly here at Berkeley.

[JESSICA HULLMAN]
No, I was at,  

on sabbatical here, actually, so it is--

[MODERATOR]
It's okay, so I'm,  

all right, I'm not, we have Jessica Hullman 
coming in from Northwestern. She is the Gini  

Rometty Professor of Computer Science and a 
fellow at the Institute for Policy Research,  

a place near and dear to my heart, at Northwestern 
and has done, well researched all of the topics  

we've been talking about for this workshop. So I'm 
really excited you would return to paper today.

[JESSICA HULLMAN]
Okay. Thank you. Yeah.

So yeah. I thought I'd give kind of a 
talk that's gonna cover a few papers,  

so it's a little higher level.

But I wanna talk about some frameworks we've been 
developing using decision theory to try to get  

more insight into human AI collaborations, 
including what's going wrong and how can we  

potentially improve these. And so I would say that 
the motivation for the work we've been doing in my  

lab for the last maybe two years is a few robust 
empirical observations. So the first, dating back  

to like '40s and 1950s observed by authors such 
as Paul Meehl, is that when you have some decision  

task or prediction task in some domain where you 
have human experts, like medical decision-making,  

if you train a statistical model on what you 
think the relevant data is, so you get some  

historical data, you train the model, the model 
will do as well or better than the human experts.

And this is very robust. There have been 
meta-analyses showing this across many  

different studies. And on the one hand, as Ben 
mentioned yesterday, this is not super surprising.

So by the time you identify, like, what 
is, what are the relevant features,  

what is the actual outcome we're trying to 
predict here, and you train a statistical model,  

then it's gonna be hard for humans to 
outperform that because you're sort of  

defining sort of optimal learning from that 
data for minimizing loss over the population,  

if that's your evaluation criteria. But 
I think it's sort of disturbing to people  

because we do have such strong intuitions 
about humans having valuable information.  

They might have private information that's 
hard to encode in a statistical model.

They can interact with the patient. 
They can observe, you know, these  

features that would be hard to encode 
through gesture, et cetera. And so today,  

we see attempts to get the best of both worlds 
by pairing humans with AI models and the goal,  

if you look at a lot of the literature, is 
what is called complementary performance.

So we wanna see the AI-assisted human do better 
than the AI alone or the human alone But there's  

another robust result from studies over the last 
10 years or so where people have been doing many  

studies to study humans who are assisted by 
AI and what we often see is more like this.  

So whenever the AI is a higher performance 
on that, in that domain than the human,  

than we tend to see the human with 
the AI doing worse than the AI alone.

And this, you know, has inspired a whole bunch 
of different attempts to sort of intervene and  

improve the human's use of the AI. So we have many 
explanation techniques and other interventions  

which are generally based on researchers' 
intuitions about what might be going wrong and  

you know, what might help. So my goal in the kind 
of work I'm gonna present today has been to try  

to disambiguate certain sources of confounding in 
these kinds of results by using decision theory  

to sort of first formalize, like, what are we, 
what is the actual decision problem that this  

human is facing and then examine their observed 
performance relative to decision theoretic sort  

of benchmarks that define kind of the best case 
decision-making we could see in that situation.

So let me start with some work we did trying to 
address this question of appropriate reliance on  

AI. So a lot of authors were asking, you know, 
"Are people appropriately relying," and yeah,  

trying to show that, in fact, we see a lot 
of over-reliance. But one of the problems  

with the typical sort of evaluation setup 
is that you might get a result like this  

that we see a lot where the human with 
the AI does worse than the AI alone,  

but it's often unclear sort of exactly how bad 
this is because we don't know what was sort of  

the best attainable performance on this 
decision problem that we could have seen.

So is that truly what the AI did, or was there 
actual room for the human to add here and they  

really failed badly? And similarly, even when we 
see the human with the AI doing better than the  

AI alone, we still don't know how good this is. 
So, you know, are they pretty close to the best  

possible performance we could expect on this 
decision problem given the human's knowledge,  

given the AI's knowledge, or is there 
still, you know, a long way to go?

And one of the problems in a lot of these studies 
that have established this sort of finding that  

humans you know, are bad at relying on AI is 
that they use as the measure for evaluation  

you know, measures based on post hoc 
accuracy. So they're sort of assuming  

that the human who is appropriately 
relying will always agree with the  

AI when it turns out that the AI was 
correct and will always disagree when  

it turns out that the AI was incorrect. 
But there's a few problems with this.

So one, you know, typically these are 
decision tasks under uncertainty. So at  

the time of the decision, the decision-maker 
has limited information, and so, you know,  

getting 100% accuracy in hindsight is 
often simply not attainable, even by  

the best-case decision-maker. Another problem 
is that this can confound different types of  

errors that humans can make relative to 
sort of the best-case decision performance.

So one type of error is simply they're over or 
under-relying relative to what would be optimal,  

but there are other types of errors related 
to sort of when they're relying on the AI  

that we can't really disambiguate when we're 
using these sort of coarse measures of,  

you know, post-hoc accuracy. And so the goal 
in this first project is gonna be to quantify,  

you know, what is the theoretical value 
of pairing a human and a model for some  

particular decision problem where we have 
human experts and we have an AI model? And  

we want to compare that to a lower bound, which 
is gonna represent the best-case performance.

If you did not have both agents, you only had the 
better-performing agent in isolation. We'll call  

this the value of complementation, it's sort 
of the maximum boost you could get in decision  

performance on that task if you had access to the 
additional agent over the better of the two alone.  

And then we'll observe the actual humans in this 
domain using the AI, and we will look at how close  

they come to this benchmark, and we will attempt 
to sort of diagnose what might be going wrong.

So we'll separate out a couple different 
types of errors by creating another benchmark  

to disentangle those. All right, so 
I'll give just sort of a high-level  

overview of the problem setup here. So we 
are considering three different roles that  

occur in sort of your typical 
AI-assisted decision workflow.

So first we assume, you know, we have a human. 
They have some signal. So I'm gonna use diagnosis  

medical diagnosis as an example 'cause 
it's a simple one throughout this.

So let's say we have a doctor, they are trying 
to diagnose a patient, so they have some  

representation of the instance, some signal, which 
is, you know, the patient's profile information,  

et cetera. We also assume there's an 
AI. It has some signal representation,  

might be overlapping and both 
of these agents are, we assume,  

capable of coming to some independent 
judgment or forecast about this case.

So they both have some independent judgment 
about what the true condition of the patient is.  

There is a decision-maker who 
has access to these judgments  

of the different agents and needs to 
make a decision between, you know,  

going with the AI judgment versus the 
human one. And typically in real workflows,  

this decision-maker is the same human who we 
assume can come to their own independent decision.

So, you know, we have a doctor, and, you know, 
they are making the decision about whether to  

trust their own judgment or the AI. So they choose 
which one to go with. We assume there's some  

utility function or scoring rule that defines kind 
of good decision-making in this domain so that's  

just gonna be a function that takes in an action 
and a state and assigns some real valued score.

You know, the, this is a decision under 
uncertainty, so there's a payoff relevant state,  

which is gonna be, you know, what's the 
true condition that this patient has?  

And there is a data-generating process or model 
pi, which you can think of as just the joint  

distribution over the payoff relevant state 
and the signal. So whenever we go to evaluate,  

you know, human AI-assisted decision-making, we 
have to say, you know, there's some distribution  

that we think captures kind of, like, the 
distribution of instances we see in practice.

And so you are talking about that 
true joint distribution for whatever  

distribution we're evaluating on. Okay, so we 
wanna, you know, determine what is the best  

case decision that could be made in a process 
like this? And so to do that, we're gonna make  

use of this sort of convention that's often 
used in decision theory, which is the notion  

of sort of the best case decision-maker who's 
gonna be the Bayesian utility-maximizing agent.

So we assume any instance, you know, 
that this agent encounters you know,  

they're starting with prior beliefs, and we're 
assuming that they are sort of as well-informed as  

we could hope any human decision-maker could be, 
meaning they have access to the joint distribution  

for this decision problem So they know the 
prior probability that the AI versus the  

human is correct, you can think of this as. On 
any given instance, they observe the signal.

They update to the Bayesian posterior beliefs 
and then they choose the utility-maximizing  

action under those beliefs. So on any given 
instance from this distribution we care about,  

this is what the rational agent 
does. And what we wanna do then  

is define sort of the best attainable 
performance over that distribution

And so we create a benchmark which is essentially 
gonna be the expected performance or score under  

our utility function of this rational agent who, 
you know, is encountering instances and always,  

you know, choosing the score-maximizing 
action. We can then compare that to what  

we'll call the baseline. This is gonna 
be the expected performance of this  

rational agent if we constrain them 
to only deciding based on the prior.

So they know the true prior probability 
that the AI is correct, and so you know,  

they're just gonna choose the best fixed action 
every time they have to make a decision. And  

so this is what I mentioned earlier, 
this value of complementation. And so,  

you know, there's a few ways we can use 
this starting before we even deploy an AI.

So, you know, imagine we are in some setting like 
a hospital. We have some new AI model. If we can  

query the humans on, you know, instances from 
the distribution we think is relevant, get their  

independent judgments, and also query the AI, you 
know, apply it then even before we deploy the AI,  

we can ask questions like, "Well, is there a 
good reason to combine these two agents here?"

So we can ask, you know, like, "How big is this 
value of complementation relative to sort of the  

baseline performance, the expected score that 
we'd have if we just used the better of the  

two in isolation?" And I think this is useful for 
researchers too who are wanting to study reliance  

because you sort of wanna make sure you're 
studying a case where there's actually like,  

a reason to combine these agents. So I 
sort of assume that it's more complex to  

put two agents together than it is to just 
use the better of the two in isolation.

So, you know, humans suddenly have to deal 
with an AI. You know, if we could do just  

as well without putting those two together, 
we should. We can also, of course, use this  

after we've deployed the AI and we observed 
the final human decisions which are, a, here.

So as I said you know, often we don't even 
know what the benchmark is within this  

framework. We can define the benchmark 
so we can see sort of how our human  

with the AI does. But we might wanna understand,  

you know, if we see that there's still ample room 
for them to improve what they're struggling with.

And so we can distinguish two sort of 
qualitatively different types of errors  

they could make relative to sort of the optimal 
decision performance. One is that they could be  

relying on the AI at the wrong rate overall. 
So you know, relative to the rational agent,  

the benchmark which is gonna define the 
optimal rate at which you rely on the AI,  

our humans might be, you know, overall, 
you know, relying too much or too little.

Another problem, though, is that relative to the 
rational agent, they might not be relying for  

these same instances. So if you think about 
what this rational Bayesian agent is doing,  

you know, they're gonna rely the optimal 
rate at the optimal rate and the instances  

on which they rely are gonna be those where 
they're sort of the biggest possible lift in  

performance by making the better decision. 
So you can think of them as sort of sorting  

the instances and taking the top K that 
correspond to the optimal reliance rate.

You know, they're sorting them based on the 
difference in expected performance of going  

with human versus AI, and so the human could sort 
of mess up that sorting step. They can't really  

discriminate at the instance level, you know, when 
it's really in their best interest to go with AI.  

So the way that we can try to disentangle 
these is by creating another benchmark,  

which we'll call the misreliant rational 
agent benchmark, and this is gonna simply  

be the expected performance on our decision 
problem of the rational agent when we constrain  

them to rely at the same rate that we 
observe the humans relying on the AI.

So this misreliant benchmark we can 
then look at and we can look at the  

remaining span between the rational agent 
benchmark and this misreliant benchmark,  

and this gives us sort of an estimate of, like, 
how much loss in performance here is due to the  

fact that humans are simply over or under-relying 
relative to the optimal rate. This remaining span  

between the observed human AI performance and 
the misreliant benchmark is then a measure of  

sort of how much, you know, score or utility 
is lost because they don't know when to rely  

or they're having trouble discriminating at an 
instance level you know, when it's the biggest  

sort of difference between the human and the 
AI. Okay, and so, you know, why is this useful?

Well, one of the things besides sort of 
looking at existing studies and trying  

to figure out what was actually going on, I 
think one of the things that is, you know,  

often challenging is that you might have 
some human using an AI And you know that  

they could do better But you don't know, 
like, what to even intervene on first.

So, you know, I'm not gonna be able to sort 
of change the interface, you know, without  

probably affecting both of these types of loss, 
but the high-level idea is that if I know that,  

like, the bigger source of loss is reliance 
loss, that might mean that the interventions I  

think about are those that are gonna, like, help 
the human over or sorry, you know, trust the AI  

more or less in general, like maybe some basic 
education, whereas if it's discrimination loss,  

I might take a closer look at the actual interface 
that I'm using to present the AI prediction,  

think about, like, how do I help them at an 
instance level better way, like their own sort  

of knowledge versus what the AI's giving them. 
And so we can apply this to existing studies  

which we have done. So we've taken some, 
you know, highly-cited papers on, sorry.

[AUDIENCE MEMBER TWO]
I have a quick question.

[JESSICA HULLMAN]
Sure, yeah.

[AUDIENCE MEMBER TWO]
On the previous slide?

[JESSICA HULLMAN]
Yeah.

[AUDIENCE MEMBER TWO]
Is it clear that the reliance  

loss and discrimination loss are totally 
orthogonal? Because it seems like when the  

human has trouble distinguishing 
at the instance level, it will.

[JESSICA HULLMAN]
Yeah. No, they're not,  

is what I'm saying. They're not totally, I mean,

yeah, we're just measuring sort of like, you 
know, if they had relied perfectly rate-wise,  

how much better would they have done and 
then trying to separate that. So it's really,  

it's just sort of, I think of it more as, like, 
hermeneutics. Like, we're trying to just, like,  

get an interpretation that will allow us 
some insight into what might be going on  

rather than sort of, you know, 
these clearly separable things.

So yeah, that's important.

[AUDIENCE MEMBER TWO]
Tenements.

[JESSICA HULLMAN]
Tenements. Okay. Can I ask one clarification?

Sure. The reliance is it the joint probability 
of disagreeing and the human following the AI,  

or is it conditioned on disagreement? Yeah, it 
has to be conditioned on disagreement because  

you can't really talk about reliance 
when they're both saying the same thing.

So yeah, we're only looking at those cases where 
they disagree. That's a good question. Okay.

So yeah, I guess very briefly, we can 
apply this to existing studies. One  

of the things we see is that some 
of these really well-cited papers,  

like the potential for complementarity was 
low to begin with. This is not an example.

This was a study by Bansal et al. They had a 
few different tasks. One of them was, like,  

LSAT performance which we're looking at here.

And so you can see that, like, the green 
versus the dark gray gives us the value of  

complementation, and it was pretty large here, so 
this was a good situation to study. But when you  

look at the behavioral performance, there's still 
sort of a long way to go towards sort of the best  

possible, you know, performance these agents 
could have seen. And so when we then create  

the mis-reliant benchmark, we see that, you 
know, overall, people are not losing out on  

a lot of sort of you know, performance 
because they're over or under-relying.

It's actually, you know, more related to their 
ability to sort of discriminate when to rely  

or when it's kind of the biggest gain. And this 
was in contrast to sort of how the original  

authors interpreted their results. They said 
this was really just a problem of reliance.

And so yeah, we can sort of get more insight 
into the existing literature from these kinds  

of techniques. All right, so in the remaining 
time, let me briefly talk about some other  

directions in the same sort of space of applying 
decision theory to try to figure out what's going  

on with humans and AI. I'm gonna go back to 
this, an original question I started with  

which is that, you know, and just sort of 
emphasize that often, you know, we think  

that humans have some additional valuable 
information, but it's often very ambiguous.

You know, what is that information they have or 
what is the value of that private information they  

might have? How might they be using the available 
contextual information relative to AI models,  

like are there features that they're 
not exploiting as well as they could?  

These kind of things are often 
hard to get some insight into.

And so in this last project, you know, we were 
mostly just evaluating information value and we  

were looking at this sort of very constrained 
decision problem where the decision is simply  

to go with the AI or the human and, you know, 
defining the value of complementary information  

that way. What we now want to do is just slightly 
generalize this. So we want to be able to say,  

like, what is the additional boost in 
best-case decision performance we could  

get if we go from sort of the rational 
agent who observes only some set of agent  

decisions for this problem to the rational 
agent who observes those agent decisions  

and some additional subset of information 
that, you know, is contextually available?

So maybe we want to know, like, 
are the human decision makers,  

do they appear to already be sort of 
using information synonymous with some  

feature that we know is available to them? 
We can ask questions of that form. Again,  

we're assuming a data during model here, which 
is just gonna be a big joint distribution.

And here you can think of, you 
know, we have the agent decisions  

And then we have a bunch of basic signals, 
which might be like features of the instance,  

there might be other agent decisions that we 
treat as a basic signal. But the idea is we  

want to condition on some focal agents and figure 
out the value of additional pieces of information.

And I guess an implicit assumption 
here is that we use is coming--or  

is common in information economics, which 
is that any information that is available  

to an agent will be revealed through 
variation in their judgments. So we're--  

that's why, you know, by looking at the 
decisions that the humans or the AIs made,  

we're sort of getting a sense of sort of the 
information that they have access to. All right.

So yeah, there's various questions we can ask 
within this kind of framework, like, you know,  

what available contextual information are 
they not exploiting that they could, you know,  

potentially get value from for this decision 
task? What is the value of the human's private  

information after we already observe, you know, 
all of the features of an instance? It's a way  

of sort of getting a sense of like, are they 
bringing something that we are not aware of?

And we can do things like try to compare 
information use between agents. I should  

mention that, you know, like there is some nuance 
for this kind of thing. So one of the things,  

you know, that you have to do is decide what 
are the basic signals in your environment.

And so if you have like very high dimensional, 
you know, signals like images or text,  

typically you want to use some coarsened set 
of features as your basic signals. So there's  

with high dimensional signals, there's 
like a extra degree of freedom. And so  

typically you would want coarsened signals 
that are kind of like human interpretable.

So some of the work in like the interpretability 
community becomes relevant here. Another nuance  

though is that, you know, like when you see 
that this agent complementary information value  

is small, you sort of have to be careful on how 
you interpret it. So let me just give an example.

So one of my colleagues at Northwestern has 
done studies with dermatologists both sort of  

specialists as well as primary care physicians. 
And one of the questions they were interested in  

is, you know, do these dermatologists appear to 
be using skin color when they make diagnoses? And  

they had an AI model as well and they wanted to 
sort of get a sense of like, you know, how much  

were these dermatologists potentially, you know, 
responding to skin color relative to this model.

So we can do this kind of look at the agent 
complementary information value where we condition  

on different types of human agents or an AI agent 
and see like what's the added value of skin color  

for this decision problem. And what we found 
was that the ACIV was smaller for these humans  

than it was for the AI model. So the AI model, you 
know, had more value to gain from this skin color.

So it was, you know, to some extent using 
information or not using that information  

as much. But because ACIV is small for the 
humans, you know, that might mean that, you know,  

either that signal doesn't have a lot of relevant 
information for the decision problem. So it could  

just be that it's not useful, like it's not gonna 
help you, you know, figure out the right decision.

Or it could be that they are already using that 
information or equivalent information. And so,  

you know, you sort of have 
to interpret what this means,  

also look at the independent value of the signal 
to try to get a sense of like, is this actually  

a valuable signal for this decision task? And 
then you could try to sort of disambiguate.

So yeah, So there's a little like 
nuance in the interpretation.

You can't just conclude like, these 
agents must be using this signal. Okay,  

so I'm probably running out of time. I'll 
just briefly highlight a few applications.

So I think, you know, for a lot of this work 
we're trying to get insight into what might be  

going wrong or what humans might be leaving 
on the table in order to intervene. And we  

want to intervene And then we want to see that 
we can actually improve decision performance.

And so some of the ways we've used this 
complementary information definition  

are first to select models. So, you 
know, often we have multiple highly  

performing AI models that we could deploy 
to help, say, doctors. But we can look at,  

you know, which one is likely to offer 
the most complementary information value.

And what we find doing this for a few medical 
tasks is that often the best model in terms of  

accuracy is not the one that's gonna complement 
the humans the best. We can also use this as  

a way of adapting or designing 
new explanations that, you know,  

are going to highlight for the human the, not 
just the information that some AI model is using,  

but the information the AI model is 
using that is most distinct from what  

they appear to already know. So I'll 
just briefly, I guess, show an example.

So I think the problem with a lot of 
explanation techniques is that first  

they only explain sort of what 
the features the AI relied on,  

so this is a common class of explanations. But 
those features may not be that relevant for  

the decision problem at hand. And, you know, 
what the explanation highlights doesn't take  

into account what we might already have observed 
about what information the humans seem to have.

So what information already appears to be sort 
of encoded in their judgments. And so we define  

essentially an instance level definition of 
complementary information value, which gives  

us sort of a sense of like how much room is 
there for specific decisions to be improved  

through better use of a specific signal. I'm 
just gonna skip over the details for time.

But what we can do then is use complementary 
information to, for instance, adapt existing  

explanation techniques so that they highlight 
information being used by the AI that is most  

distinct from what the humans appear to be 
already aware of. And so this is an excerpt  

from a SHAP explanation. This last column 
was just the SHAP values, and I cut it off.

There were more features, but we had an 
experiment where we had people doing house  

price prediction. And so in one condition we 
just showed them SHAP. In another condition,  

all we did was use the complementary 
information value definition in order  

to sort the different features, and 
then we highlighted the top few.

And what we found was that we actually saw, 
you know, measurable differences in decision  

performance just from this sort of simple, 
you know, highlighting step. So we were  

looking at how much they improved relative to 
independent human judgments, which we collect  

in these experiments as well. And relative 
to SHAP, there was 25% more of an improvement  

simply from, you know, passing this through this 
kind of filter based on complementary information.

Final thing that we're doing that 
I think is sort of interesting is  

actually trying to design complementary 
agents, like language model agents by  

fine-tuning them using this notion of 
complementary information value so that  

they can sort of help humans extract or help the 
decision-makers extract information in a text that  

we have available at the time of some decision 
that the humans might not be exploiting. So Yeah.

So there, here's just sort of a quick diagram, 
but what we're doing here is assuming a  

decision-maker, they have some unstructured text 
available to them. So to use a medical example,  

we might have some doctor, they have access to 
a radiology report. They also see a radiology  

image, and they might see some agent 
decision, like an AI model's decision.

We assume that text you know, contains 
latent signals that are relevant for the  

decision problem. So again, we just have utility 
function and a decision problem we've defined. And  

what we wanna do is basically fine-tune an LLM 
using reinforcement learning-based fine-tuning  

so that it outputs the signals that 
are relevant to that decision task,  

which, you know, for instance, 
might be like cardiac dysfunction  

diagnosis but are not necessarily captured 
by the information in the AI prediction.

So we're kind of trying to 
show the decision-maker like,  

"Here's some stuff that this AI model 
doesn't appear to be getting." So this,  

you know, I think there's many applications for 
these kind of things. So these medical examples  

for instance, but we're also looking at cases 
like, you know, you have humans who are making  

very tough decisions like social workers 
deciding when to remove children from homes.

And they have access to a whole bunch 
of text data, like call transcripts.  

But you know, any given social worker may be 
sometimes missing information that's relevant  

that predicts sort of when the children 
actually need to get removed. And so  

that's one, and another one we're doing 
is looking at Wikipedia article edits.

So on Wikipedia there's algorithmic sort of 
or a, a machine learning model I think called  

LiftWing that is basically looking at each 
edit and deciding whether to approve it or  

not. But then that model's decisions have to be 
overseen by some actual human moderator. And so  

what we're doing is, you know, pulling out what's 
the information in this revision, this article  

revision, that will most predict whether the 
moderator should, you know, revert that decision.

All right. So I will close there. I think the 
high-level takeaway is just that to understand  

human-AI or AI-assisted decisions, we 
really need to sort of understand and  

clarify what's the decision problem we are 
studying and what is attainable within that.

And then we can start to ask a 
number of questions about the  

value of different pieces of information. Thanks.

(audience applauding)

[MODERATOR]
Thank you so much. Have time  

for one or two questions before 
the break. We'll start with Duncan.

[DUNCAN]
Thank you. Lots of  

interesting leads. One question I have, when you 
have the human, well, let me ask differently. In  

one of your settings, was there a situation where 
the human in order to override the AI decision?

[JESSICA HULLMAN]
Mm-hmm.

[DUNCAN]
Had to do  

work more than just saying, "I don't think 
it's right." Because, and I, the reason--

[JESSICA HULLMAN]
In most, yeah.

[DUNCAN]
I ask is  

because we tried to experiment with 
this a little, and we found that  

there's another cognitive process. As soon 
as it's more work, they're reluctant to--

[JESSICA HULLMAN]
Yeah.

[DUNCAN]
Disagree with the AI, you know?

[JESSICA HULLMAN]
Yeah, I think there's  

a lot of that, yeah. In the kind of 
situations we've looked at. Yeah,  

we're not, I guess that's not something 
that we've specifically tried to understand.

We're really just sort of looking at, you know, 
datasets where you have the independent human  

judgment 'cause it's becoming more and more 
common in these workflows to first, like,  

have the human make their prediction before you 
show them the AI. So we're just assuming a certain  

setup, and you know and then 
running our own experiments  

sometimes that have this setup. So yeah, 
but that's-- I know these, there's lots

[DUNCAN]
But they have done the work  

anyway already. Yeah, gotcha.

[JESSICA HULLMAN]
Yeah, Mm-hmm.

[DUNCAN]
I have a question. Part of your time  

out there, in terms of the value of information, 
reminded me of very old work by Eric Horvitz.

[JESSICA HULLMAN]
Yeah.

[DUNCAN]
Which looked at value of surprise  

for like, do you think of 
it in the same line of work?

[JESSICA HULLMAN]
Yeah, I think it's  

related. Yeah. We're coming 
more from, I guess, like,  

an econ theory perspective a little 
bit compared to that, but there's,

yeah, it's very similar. I 
mean, it's all decision theory.

A lot of the stuff we're doing with defining 
value of information, there is sort of area  

of information economics that does a lot of this. 
And so some of the assumptions we make are those  

that are common there, but otherwise very related. 
And I've talked to Eric, yeah, a lot about this.

I hope he's a fan. That's what he tells me.

[MODERATOR]
All right, let's take one last one.

[AUDIENCE MEMBER TWO]
Yeah. So I, I'm curious about something  

that I, I think is related to the contextual 
setting that you're, that you were talking  

about. 'cause it seems like a lot of the settings 
where people have sort of, like, high hopes for,  

like, human AI complementarity and avoiding this, 
like, you know, like clinical statistical judgment  

kind of thing is where humans, like, 
actually have more information, right?

[JESSICA HULLMAN]
Yeah.

[AUDIENCE MEMBER TWO]
And so to get at that,  

like, do you think that we need to observe the 
human's full information set experimentally,  

right? Because then it's like exactly 
this, the settings that we wanna look  

at are the ones where we can't 
measure it well basically, but--

[JESSICA HULLMAN]
Yeah. I don't think  

you do. I think we're trying to, like, get 
at, like, the most you can do without that.

Obviously that could be helpful, but 'cause I 
can't tell humans that they are not exploiting  

some private signal well enough because I don't 
know their private signals. All I can say is,  

like, you know, they're-- they appear 
to have more information than, say,  

like, the full feature representation 
that is available to the AI model.

So you can test for, yeah, if they have more in 
terms of value. But no, I don't--I think you can  

do a lot without knowing it, but certainly 
you can do more once you know it. Um, so

Yeah, I'm curious if you have specific 
examples in mind. Maybe we can chat.

[MODERATOR]
All right.  

That's a good segue. So let's thank our speaker.

[JESSICA HULLMAN]
Thanks.

(applause)

[MODERATOR] 

I believe it's time for our break, right? 
Am I--I'm now looking at other--Yeah,  

Time for our break. So we'll have a 25-minute 
break 'cause we started five minutes past.


