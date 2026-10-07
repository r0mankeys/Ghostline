# Ghostline

> A coach that bridges the gap between my art goals and my current abilities by giving daily drills and critiquing what I draw

### My goal: 
Draw dynamic characters from imagination, with realism, in mixed media (pen plus paint or colour).

### My level:
Decent at copying, weak at constructing from imagination. That points the roadmap at construction fundamentals first.

## MVP

1. I enter my goal and self-assessed level once. An LLM drafts a 12-week roadmap that I can edit.
2. I see today's drills, taken from the roadmap's current week.
3. I print the matching drill sheet for each drill.
4. I upload a phone photo of the finished sheet. The app flattens it and scores lines and ellipses.
5. I get a written critique that uses those scores and the drill's rubric.
6. I see my past submissions and how their scores change over time.

## Milestones

- [ ] Walking skeleton. A phone page uploads a photo to FastAPI, which saves it to storage and adds a row in Postgres, deployed and working from my phone. About 4–6 h.
- [ ] First critique. Claude critiques an uploaded photo with no CV yet, and the structured result is saved. About 3–4 h.
- [ ] Roadmap. A goal and level form generates a 12-week roadmap and stores it. About 3–4 h.
- [ ] Today view. It shows this week's drills. About 2 h.
- [ ] History. A list of past submissions. About 2 h.
Phase B: computer vision
- [ ] Drill sheet. A printable PDF template with corner markers and light-blue targets. About 2–3 h.
- [ ] Flatten. Detect the markers and warp the photo flat to a known scale. About 4–6 h.
- [ ] Line scoring. Isolate the ink and measure each line's wobble and its distance from the target points. About 6–10 h.
- [ ] Ellipse scoring. Fit each ellipse and measure fit error and axis alignment. About 6–8 h.
- [ ] Grounded critique. Feed the scores into the critique prompt and chart them in History. About 2–3 h.
- [ ] Eval. Hand-grade 20 of my own pages and compare them with the CV and LLM output, then tune. About 4 h.
- [ ] Use it. Drill 14 days in a row through the app.
