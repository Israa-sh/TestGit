# HW - 3 : Determine if two text paragraphs are relevant
# This HW done by : Isra AL-Sharapati
# Date : 8-2-2020

input_1_text = """
Are the technologies that surround us tools that we can identify, grasp and consciously use to improve our lives? 
Or are they more than that: powerful objects and enablers that influence our perception of the world, change our 
behaviour and affect what it means to be human?
Technologies are emerging and affecting our lives in ways that indicate we are at the beginning of a 
Fourth Industrial Revolution, a new era that builds and extends the impact of digitization in new and unanticipated 
ways. It is therefore worthwhile taking some time to consider exactly what kind of shifts we are experiencing and how 
we might, collectively and individually, ensure that it creates benefits for the many, rather than the few.
When were the other industrial revolutions? The First Industrial Revolution is widely taken to be the shift from our 
reliance on animals, human effort and biomass as primary sources of energy to the use of fossil fuels and the mechanical 
power this enabled. The Second Industrial Revolution occurred between the end of the 19th century and the first two decades 
of the 20th century, and brought major breakthroughs in the form of electricity distribution, both wireless and wired communication, 
the synthesis of ammonia and new forms of power generation. The Third Industrial Revolution began in the 1950s with the development 
of digital systems, communication and rapid advances in computing power, which have enabled new ways of generating, processing and 
sharing information. The Fourth Industrial Revolution can be described as the advent of “cyber-physical systems” involving entirely 
new capabilities for people and machines. While these capabilities are reliant on the technologies and infrastructure of the Third 
Industrial Revolution, the Fourth Industrial Revolution represents entirely new ways in which technology becomes embedded within societies 
and even our human bodies. Examples include genome editing, new forms of machine intelligence, breakthrough materials and approaches to 
governance that rely on cryptographic methods such as the blockchain. As the novelist William Gibson famously said: 
“The future is already here – it's just not very evenly distributed.” Indeed, in many parts of the world aspects of the Second and Third 
Industrial Revolutions have yet to be experienced, complicated by the fact that new technologies are in some cases able to “leapfrog” older 
ones. As the United Nations pointed out in 2013, more people in the world have access to a mobile phone than basic sanitation. In the same 
way, the Fourth Industrial Revolution is beginning to emerge at the same time that the third, digital revolution is spreading and maturing 
across countries and organizations. The complexity of these technologies and their emergent nature makes many aspects of the Fourth 
Industrial Revolution feel unfamiliar and, to many, threatening. We should therefore remember that all industrial revolutions are 
ultimately driven by the individual and collective choices of people. And it is not just the choices of the researchers, inventors 
and designers developing the underlying technologies that matter, but even more importantly those of investors, consumers, regulators 
and citizens who adopt and employ these technologies in daily life. The Fourth Industrial Revolution may look and feel like an 
exogenous force with the power of a tsunami, but in reality, it is a reflection of our desires and choices. At the heart of discussions 
around emerging technologies there is a critical and central question: what do we want these technologies to deliver for us?


""".lower()

input_2_text = """
The Fourth Industrial Revolution heralds a series of social, political, cultural, and economic upheavals that will unfold 
over the 21st century. Building on the widespread availability of digital technologies that were the result of the Third Industrial, 
or Digital, Revolution, the Fourth Industrial Revolution will be driven largely by the convergence of digital, biological, and physical 
innovations. Like the First Industrial Revolution’s steam-powered factories, the Second Industrial Revolution’s application of science 
to mass production and manufacturing, and the Third Industrial Revolution’s start into digitization, the Fourth Industrial Revolution’s 
technologies, such as artificial intelligence, genome editing, augmented reality, robotics, and 3-D printing, are rapidly changing the way 
humans create, exchange, and distribute value. As occurred in the previous revolutions, this will profoundly transform institutions, 
industries, and individuals. More importantly, this revolution will be guided by the choices that people make today: the world in 
50 to 100 years from now will owe a lot of its character to how we think about, invest in, and deploy these powerful new technologies.
It’s important to appreciate that the Fourth Industrial Revolution involves a systemic change across many sectors and aspects of 
human life: the crosscutting impacts of emerging technologies are even more important than the exciting capabilities they represent. 
Our ability to edit the building blocks of life has recently been massively expanded by low-cost gene sequencing and techniques such as 
CRISPR; artificial intelligence is augmenting processes and skill in every industry; neurotechnology is making unprecedented strides in 
how we can use and influence the brain as the last frontier of human biology; automation is disrupting century-old transport and 
manufacturing paradigms; and technologies such as blockchain and smart materials are redefining and blurring the boundary between the 
digital and physical worlds. The Fourth Industrial Revolution is therefore not a prediction of the future but a call to action. 
It is a vision for developing, diffusing, and governing technologies in ways that foster a more empowering, collaborative, and 
sustainable foundation for social and economic development, built around shared values of the common good, human dignity, and 
intergenerational stewardship. Realizing this vision will be the core challenge and great responsibility of the next 50 years.
We cannot foresee at this point which scenario is likely to emerge from this new revolution. However, I am convinced of one thing—that 
in the future, talent, more than capital, will represent the critical factor of production.
With these fundamental transformations underway today, we have the opportunity to proactively shape the Fourth Industrial 
Revolution to be both inclusive and human-centered. This revolution is about much more than technology—it is an opportunity 
to unite global communities, to build sustainable economies, to adapt and modernize governance models, to reduce material and 
social inequalities, and to commit to values-based leadership of emerging technologies.
""".lower()

print(input_1_text)
print()
print(input_2_text)
