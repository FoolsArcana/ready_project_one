df = read.csv("reduced_health_Survey_GW.csv", header = T)

library(psych)

# Race dummies
df$black = ifelse(df$healask == "Black non-hispanic",
                  1,0)
df$hisp = ifelse(df$healask == "Hispanic",
                  1,0)
df$white = ifelse(df$healask == "White non-hispanic",
                  1,0)

# Gender - male = 0
df$sex01 = ifelse(df$sex == "Male", 0,1)
table(df$sex01)
table(df$sex)

# BMI missing

df$bmi[df$bmi == 99.9] <- NA
describe(df$bmi)

# Age missing
df$age[df$age == "Refused"] <- NA
df$age <- as.numeric(df$age)

# Fruit/veg missing
df$heal13[df$heal13 == "Don't know" |
          df$heal13 == "Refused"] <- NA

table(df$heal13)


# Educ as continuous
library(car)
df$educ_cont <- recode(df$educ, "
                       'Less than high school graduate' = 1;
                       'High school graduate' = 2;
                       'Some college' = 3;
                       'Graduated college' = 4;
                       'Graduate school or more' = 5;
                       'Technical school/other' = NA; 'Refused' = NA")
df$educ_cont <-as.numeric(df$educ_cont)
table(df$educ_cont)


# Walkability pred BMI

walk_bmi = lm(df$heal10min ~ df$bmi)
summary(walk_bmi)


# Odds of fruit/veg expense by race
fruit_race = glm(heal13 ~ black + hisp + age + sex01 + educ_cont,
                 data = df, family = "binomial")
summary(fruit_race)
exp(coef(fruit_race))

# BMI differs by ease of food access
t.test(df$bmi ~ df$heal13)

# BMI differs by food access and race
summary(lm(df$bmi ~ df$heal13 + df$black + df$hisp))
