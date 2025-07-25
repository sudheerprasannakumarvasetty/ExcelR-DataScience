# Association Rule Mining - Market Basket Analysis

This project implements **Association Rule Mining** using the **Apriori algorithm** on the Online Retail dataset to discover patterns in customer purchase behavior.

---

## Dataset

- **Name**: Online Retail (Provided as `Online retail.xlsx`)
- **Format**: Each row is a list of items purchased together in one transaction.
- **Source**: Provided by instructor.

---

## Objective

- Perform **Market Basket Analysis** using Association Rule Mining.
- Discover relationships between items frequently bought together.
- Generate actionable insights using **support**, **confidence**, and **lift**.

---

## Data Preprocessing

- Removed empty rows.
- Split comma-separated item lists into Python lists.
- Transformed the data into a **one-hot encoded format** using `TransactionEncoder` from `mlxtend`.

---

## Algorithms Used

- **Apriori Algorithm**: To generate frequent itemsets.
- **Association Rule Mining**: To generate rules using `support`, `confidence`, and `lift`.

---

## Key Code Steps

1. **Load Data** from Excel using `pandas`
2. **Split Transactions** into item lists
3. **Encode Items** using `TransactionEncoder`
4. **Apply Apriori** with `min_support=0.01`
5. **Generate Rules** using `association_rules()` with `metric='lift'`

---

## Results & Insights

- Generated rules with high lift indicate **strong associations** between items.
- Example: If a customer buys `green tea`, they are **2.5x more likely** to also buy `honey`.
- Insights help create combos, offers, and product placements.

---

## Interview Questions & Answers

### 1. What is Lift and Why is it Important?

**Lift** measures how much more likely items A and B are bought together than if they were independent.

- Lift > 1 → Positive association  
- Lift = 1 → No association  
- Lift < 1 → Negative association  

> Helps identify non-random, meaningful item relationships.

---

### 2. What is Support and Confidence?

support
(
𝐴
→
𝐵
)
=
Transactions containing both A and B
Total transactions
support(A→B)= 
Total transactions
Transactions containing both A and B

confidence
(
𝐴
→
𝐵
)
=
Transactions containing both A and B
Transactions containing A
confidence(A→B)= 
Transactions containing A
Transactions containing both A and B
​
 
They measure how frequent and how reliable a rule is, respectively.

> Support = frequency of the rule  
> Confidence = reliability of the rule

---

### 3. Limitations of Association Rule Mining

- Too many rules (noise).
- Requires manual threshold tuning.
- Doesn’t consider time or sequence.
- High computational cost on large datasets.
- Ignores context like user behavior or seasonality.

---

## Conclusion

Association Rule Mining is a powerful unsupervised learning technique for finding product relationships in retail. This project demonstrates its application using real-world data with interpretable and actionable results.



