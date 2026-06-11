# Example Mapping Output Format

Use this text-based format to record the results of an Example Mapping session. 

## [STORY] Earning Frequent Flyer points from flights
*In order to improve customer loyalty*
*As an airline sales manager*
*I want travelers to earn Frequent Flyer points when they fly with us*

### [RULE] Flights within Europe earn 100 points
* **[EXAMPLE]** The one where Tara flies economy from Paris to Berlin.
* **[EXAMPLE]** The one where Tara flies economy from London to New York (Negative case).

### [RULE] Flights outside Europe earn 1 point every 10 km
* **[EXAMPLE]** The one where Tara flies economy from London to New York (5500 km = 550 points).

### [RULE] Business flights earn an extra 50%
* **[EXAMPLE]** Betty flies business from Paris to Berlin => 150 pts.

### [RULE] Silver Frequent Flyer members earn an extra 25%
* **[EXAMPLE]** Silvia is a Silver Frequent Flyer. Silvia flies economy from Paris to Berlin => 125 pts.

---

## [QUESTIONS]
* **[QUESTION]** Does this only include flights in the European Union, or all of geographical Europe?
* **[QUESTION]** Do flights purchased with points earn points?

## Story Status: BLOCKED
There are critical business questions that must be answered by the Product Owner before development begins.
