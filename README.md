# PERT (Program Evaluation and Review Technique)
PERT - A project evaluation and analysis method that is used in project management.
> [!IMPORTANT]
> In probability and statistics, the PERT distributions are a family of continuous probability
> distributions defined by the minimum (O - optimistic), most likely (M - nominal) and maximum (P - pessimistic) values that a variable can take.
> It is a transformation of the four-parameter beta distribution with an additional assumption that its expected value is
![formula](https://avatars.mds.yandex.net/i?id=8ecd57bcf8f14b97cdb8cf14f40ff0c4461e4879-11004153-images-thumbs&n=13)

We can calculate deviation (σ) for task.
> [!IMPORTANT]
> σ is the standard deviation of the task execution time distribution. In fact, this is a measure of the uncertainty of the task: if
> this number is large, then the uncertainty is also large.
>
> ```math
> σ = \frac{P - O}{6}
> ```

Also we can summarize for all tasks.
> [!IMPORTANT]
> For any sequence of tasks, the estimated duration of execution is calculated by simply summing the durations of all tasks in the sequence.
>
> The standard deviation of the sequence is equal to the square root of the sum of the squares of the standard deviations of the problems.
> 
> ```math
> E\left(\text{{sequence}}\right) = \sum_{} E\left(\text{{task}}\right)
> ```
>
> ```math
> σ\left(\text{{sequence}}\right) = \sqrt{\sum_{} σ\left(\text{{task}}\right)^2}
> ```

## Using
```
git clone https://github.com/deadloveskih/PERT-Program-Evaluation-and-Review-Technique-.git
```
Open project in terminal and:
```
python main
```
Then
```
pert: help
```

## Learn more
[Wikipedia](https://en.wikipedia.org/wiki/PERT_distribution)
[Wikipedia](https://en.wikipedia.org/wiki/Program_evaluation_and_review_technique)
