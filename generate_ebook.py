#!/usr/bin/env python3
"""Generate the Bliss Gums Blood Sugar Guide PDF ebook."""

import os
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Frame, PageTemplate, BaseDocTemplate, KeepTogether
)
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# ── Brand Constants ──────────────────────────────────────────
BRAND_NAME = "BLISS GUMS"
BRAND_NAME_MIXED = "Bliss Gums"
WEBSITE = "blissgums.co"
EMAIL = "info@blissgums.co"
COMPANY = "Bliss Gums LLC"
LOCATION = "Wyoming, United States"
PRIMARY_COLOR = HexColor("#059669")
DARK_BG = HexColor("#111827")
LIGHT_GREEN_BG = HexColor("#f0fdf4")
GREEN_BORDER = HexColor("#059669")
LIGHT_GRAY = HexColor("#f3f4f6")
MEDIUM_GRAY = HexColor("#6b7280")
DARK_TEXT = HexColor("#111827")

PAGE_WIDTH, PAGE_HEIGHT = letter
MARGIN = 0.75 * inch

OUTPUT_PATH = "/Users/cillinhughes/projects/blissgums/bliss-gums-blood-sugar-guide.pdf"
COPY_PATH = "/Users/cillinhughes/projects/blissgums/digital-marketing-playbook.pdf"


# ── Chapter Content ──────────────────────────────────────────

CHAPTERS = [
    {
        "number": "01",
        "title": "Understanding Blood Sugar",
        "content": [
            ("heading", "What Is Blood Sugar?"),
            ("text", "Blood sugar, also known as blood glucose, is the primary sugar found in your blood. It comes from the food you eat and serves as your body's main source of energy. Your bloodstream carries glucose to all of your cells to provide the energy they need to function."),
            ("text", "When you eat carbohydrates, your digestive system breaks them down into glucose, which enters your bloodstream. Your pancreas then releases insulin, a hormone that acts like a key to unlock your cells so glucose can enter and be used for energy."),
            ("heading", "Why Blood Sugar Balance Matters"),
            ("text", "Maintaining healthy blood sugar levels is crucial for your overall health and well-being. When blood sugar levels remain consistently elevated, it can lead to a condition known as hyperglycemia, which over time may contribute to serious health complications including:"),
            ("bullets", [
                "Heart disease and cardiovascular problems",
                "Kidney damage (nephropathy)",
                "Nerve damage (neuropathy)",
                "Eye damage (retinopathy)",
                "Slow wound healing",
                "Increased risk of infections"
            ]),
            ("heading", "How Your Body Regulates Blood Sugar"),
            ("text", "Your body has an elegant system for keeping blood sugar within a healthy range. The pancreas produces two key hormones: insulin (which lowers blood sugar by helping cells absorb glucose) and glucagon (which raises blood sugar by signaling the liver to release stored glucose)."),
            ("text", "In a healthy person, this system works automatically to keep blood sugar levels stable throughout the day. Problems arise when the body either doesn't produce enough insulin, or when cells become resistant to insulin's effects -- a condition known as insulin resistance."),
            ("callout", "Did You Know? Approximately 1 in 3 American adults has prediabetes, and most don't even know it. Early detection and lifestyle changes can prevent progression to type 2 diabetes."),
            ("heading", "Types of Blood Sugar Disorders"),
            ("text", "There are several conditions related to blood sugar regulation:"),
            ("bullets", [
                "Type 1 Diabetes: An autoimmune condition where the pancreas produces little or no insulin",
                "Type 2 Diabetes: The most common form, where the body becomes resistant to insulin or doesn't produce enough",
                "Prediabetes: Blood sugar levels are higher than normal but not yet high enough for a diabetes diagnosis",
                "Gestational Diabetes: Develops during pregnancy and usually resolves after delivery"
            ]),
            ("text", "Understanding your blood sugar is the first step toward taking control of your metabolic health. In the following chapters, we'll explore practical strategies for monitoring, managing, and optimizing your blood sugar levels.")
        ]
    },
    {
        "number": "02",
        "title": "Reading Your Numbers",
        "content": [
            ("heading", "Key Blood Sugar Measurements"),
            ("text", "Understanding your blood sugar numbers is essential for effective management. There are several important measurements your doctor may use to assess your blood sugar health."),
            ("table", {
                "headers": ["Test", "Normal", "Prediabetes", "Diabetes"],
                "rows": [
                    ["Fasting Blood Sugar", "Below 100 mg/dL", "100-125 mg/dL", "126+ mg/dL"],
                    ["A1C", "Below 5.7%", "5.7-6.4%", "6.5%+"],
                    ["Random Blood Sugar", "Below 140 mg/dL", "140-199 mg/dL", "200+ mg/dL"],
                    ["Oral Glucose Tolerance", "Below 140 mg/dL", "140-199 mg/dL", "200+ mg/dL"],
                ]
            }),
            ("heading", "Fasting Blood Sugar (FBS)"),
            ("text", "This test measures your blood sugar after an overnight fast of at least 8 hours. It provides a baseline measurement of how well your body manages glucose when you haven't eaten. A normal fasting blood sugar is below 100 mg/dL."),
            ("heading", "Hemoglobin A1C"),
            ("text", "The A1C test provides a picture of your average blood sugar level over the past 2-3 months. It measures the percentage of hemoglobin (a protein in red blood cells) that is coated with sugar. This test doesn't require fasting and can be done at any time of day."),
            ("callout", "Important: A1C results can be affected by certain conditions including anemia, kidney disease, and some hemoglobin variants. Discuss any concerns with your healthcare provider."),
            ("heading", "Post-Meal Blood Sugar"),
            ("text", "Blood sugar levels after eating (postprandial glucose) are also important indicators. In healthy individuals, blood sugar peaks about 1-2 hours after eating and should return to near-fasting levels within 3 hours. A post-meal reading above 180 mg/dL may indicate a problem."),
            ("heading", "Understanding Your Results"),
            ("text", "Blood sugar levels can vary based on many factors including time of day, recent meals, physical activity, stress, illness, and medications. A single reading doesn't tell the whole story. Trends over time are more meaningful than any individual measurement."),
            ("text", "Work with your healthcare provider to determine your personal blood sugar targets, as these may differ based on your age, health conditions, and other factors.")
        ]
    },
    {
        "number": "03",
        "title": "Smart Eating for Blood Sugar Control",
        "content": [
            ("heading", "The Foundation of Blood Sugar Management"),
            ("text", "What you eat has the most direct impact on your blood sugar levels. Understanding how different foods affect your glucose levels empowers you to make informed choices that support stable blood sugar throughout the day."),
            ("heading", "Understanding Carbohydrates"),
            ("text", "Carbohydrates have the greatest effect on blood sugar because they are broken down into glucose during digestion. However, not all carbohydrates are created equal:"),
            ("bullets", [
                "Simple carbohydrates (white bread, sugar, candy) are digested quickly and cause rapid blood sugar spikes",
                "Complex carbohydrates (whole grains, legumes, vegetables) are digested more slowly and cause a gradual rise",
                "Fiber is a type of carbohydrate that isn't digested and actually helps slow glucose absorption"
            ]),
            ("heading", "The Plate Method"),
            ("text", "One of the simplest approaches to blood sugar-friendly eating is the plate method recommended by the American Diabetes Association:"),
            ("bullets", [
                "Fill half your plate with non-starchy vegetables (broccoli, spinach, peppers, green beans)",
                "Fill one quarter with lean protein (chicken, fish, tofu, eggs)",
                "Fill one quarter with complex carbohydrates (brown rice, quinoa, sweet potato)",
                "Add a small serving of healthy fat (avocado, nuts, olive oil)"
            ]),
            ("heading", "Foods That Help Stabilize Blood Sugar"),
            ("table", {
                "headers": ["Food Category", "Best Choices", "Benefits"],
                "rows": [
                    ["Proteins", "Fish, chicken, eggs, legumes", "Slow digestion, reduce spikes"],
                    ["Healthy Fats", "Avocado, nuts, olive oil", "Improve insulin sensitivity"],
                    ["Fiber-Rich Foods", "Vegetables, berries, oats", "Slow glucose absorption"],
                    ["Fermented Foods", "Yogurt, kimchi, sauerkraut", "Support gut health & metabolism"],
                ]
            }),
            ("heading", "Foods to Limit or Avoid"),
            ("text", "Certain foods can cause rapid blood sugar spikes and should be consumed in moderation:"),
            ("bullets", [
                "Sugary beverages (soda, juice, sweetened coffee drinks)",
                "Refined grains (white bread, white rice, regular pasta)",
                "Processed snacks (chips, crackers, cookies)",
                "High-sugar cereals and granola bars",
                "Candy, pastries, and desserts"
            ]),
            ("callout", "Tip: You don't have to eliminate these foods entirely. The key is moderation and pairing higher-glycemic foods with protein, fiber, or healthy fats to slow absorption.")
        ]
    },
    {
        "number": "04",
        "title": "Low-Glycemic Meal Planning",
        "content": [
            ("heading", "Understanding the Glycemic Index"),
            ("text", "The Glycemic Index (GI) is a scale from 0 to 100 that ranks foods based on how quickly they raise blood sugar. Foods with a low GI (55 or less) are digested slowly and cause a gradual rise in blood sugar, while high-GI foods (70 or above) cause rapid spikes."),
            ("table", {
                "headers": ["GI Category", "GI Range", "Examples"],
                "rows": [
                    ["Low GI", "55 or below", "Oats, legumes, most fruits, sweet potatoes"],
                    ["Medium GI", "56-69", "Brown rice, whole wheat bread, bananas"],
                    ["High GI", "70 and above", "White bread, white rice, potatoes, sugary cereals"],
                ]
            }),
            ("heading", "Sample Low-GI Meal Plan"),
            ("text", "Here is a sample day of blood sugar-friendly eating that incorporates low-glycemic foods:"),
            ("bullets", [
                "Breakfast: Steel-cut oatmeal with berries, walnuts, and cinnamon",
                "Mid-Morning Snack: Apple slices with almond butter",
                "Lunch: Grilled chicken salad with mixed greens, avocado, chickpeas, and olive oil dressing",
                "Afternoon Snack: Greek yogurt with a handful of almonds",
                "Dinner: Baked salmon with roasted broccoli and quinoa",
                "Evening Snack (if needed): Small handful of mixed nuts"
            ]),
            ("heading", "Meal Prep Tips for Success"),
            ("text", "Planning and preparing meals in advance is one of the most effective strategies for maintaining stable blood sugar:"),
            ("bullets", [
                "Batch cook proteins (chicken, fish, beans) on weekends for the week ahead",
                "Pre-chop vegetables and store in containers for quick meal assembly",
                "Prepare overnight oats for easy grab-and-go breakfasts",
                "Keep healthy snacks portioned and easily accessible",
                "Cook extra dinner portions for next-day lunches"
            ]),
            ("callout", "Remember: The glycemic index of a food can change based on how it's prepared. For example, al dente pasta has a lower GI than well-cooked pasta. Cooling and reheating starchy foods can also lower their glycemic impact."),
            ("heading", "Portion Control Matters"),
            ("text", "Even low-GI foods can raise blood sugar significantly if eaten in large quantities. The total amount of carbohydrates you eat at one time matters just as much as the type. A concept called Glycemic Load (GL) takes both quality and quantity into account, providing a more complete picture of a food's impact on blood sugar.")
        ]
    },
    {
        "number": "05",
        "title": "Exercise & Physical Activity",
        "content": [
            ("heading", "How Exercise Affects Blood Sugar"),
            ("text", "Physical activity is one of the most powerful tools for managing blood sugar. When you exercise, your muscles use glucose for energy, which directly lowers blood sugar levels. Additionally, regular exercise improves insulin sensitivity, meaning your cells become better at using available insulin to absorb glucose."),
            ("heading", "Types of Exercise for Blood Sugar Control"),
            ("text", "A well-rounded exercise program includes multiple types of physical activity:"),
            ("table", {
                "headers": ["Exercise Type", "Examples", "Blood Sugar Benefit"],
                "rows": [
                    ["Aerobic", "Walking, swimming, cycling", "Immediate glucose reduction"],
                    ["Resistance", "Weight training, resistance bands", "Improved insulin sensitivity"],
                    ["Flexibility", "Yoga, stretching, tai chi", "Stress reduction, circulation"],
                    ["HIIT", "Interval training, sprints", "Extended metabolic benefits"],
                ]
            }),
            ("heading", "Getting Started Safely"),
            ("text", "If you're new to exercise or have been inactive, start gradually and build up over time:"),
            ("bullets", [
                "Begin with 10-15 minute walks after meals",
                "Gradually increase duration to 30 minutes per session",
                "Aim for 150 minutes of moderate activity per week",
                "Add resistance training 2-3 times per week",
                "Always warm up before and cool down after exercise"
            ]),
            ("callout", "Safety Note: If you take insulin or certain diabetes medications, exercise can sometimes cause blood sugar to drop too low (hypoglycemia). Always carry a fast-acting carbohydrate source and monitor your levels before, during, and after exercise."),
            ("heading", "The Post-Meal Walk"),
            ("text", "One of the simplest and most effective strategies is taking a 10-15 minute walk after meals. Research shows that post-meal walking can reduce blood sugar spikes by up to 30%. This easy habit requires no equipment, no gym membership, and can be done by almost anyone."),
            ("heading", "Staying Consistent"),
            ("text", "The benefits of exercise for blood sugar management are cumulative and depend on consistency. Find activities you enjoy, schedule them like appointments, and consider finding an exercise partner for accountability. Even small amounts of movement throughout the day add up to significant benefits.")
        ]
    },
    {
        "number": "06",
        "title": "Monitoring Your Levels",
        "content": [
            ("heading", "Why Self-Monitoring Matters"),
            ("text", "Regular blood sugar monitoring gives you real-time feedback on how your body responds to food, exercise, stress, and other factors. This information empowers you to make informed decisions about your daily choices and helps your healthcare team optimize your management plan."),
            ("heading", "Blood Glucose Monitoring Tools"),
            ("table", {
                "headers": ["Tool", "How It Works", "Best For"],
                "rows": [
                    ["Finger-Stick Meter", "Small blood sample from fingertip", "Spot-checking, most affordable"],
                    ["CGM (Continuous Monitor)", "Sensor under skin reads glucose", "Seeing trends and patterns"],
                    ["Flash Glucose Monitor", "Scan sensor for reading", "Balance of convenience and cost"],
                ]
            }),
            ("heading", "When to Test"),
            ("text", "The frequency and timing of blood sugar testing depends on your individual situation. Common testing times include:"),
            ("bullets", [
                "First thing in the morning (fasting)",
                "Before meals",
                "2 hours after meals",
                "Before and after exercise",
                "Before bedtime",
                "When you feel symptoms of high or low blood sugar"
            ]),
            ("heading", "Keeping a Blood Sugar Log"),
            ("text", "Recording your blood sugar readings along with contextual information helps identify patterns and triggers. Include:"),
            ("bullets", [
                "Date and time of each reading",
                "Blood sugar value",
                "What you ate recently",
                "Physical activity",
                "Stress level",
                "Medications taken",
                "Any symptoms or unusual circumstances"
            ]),
            ("callout", "Pro Tip: Many glucose meters and CGM systems have companion apps that automatically log readings and can generate reports for your doctor visits. Take advantage of these digital tools to make tracking easier."),
            ("heading", "Understanding Patterns"),
            ("text", "After collecting data for a week or two, look for patterns. Do you consistently spike after breakfast? Does your fasting glucose run high? Do certain foods cause bigger spikes than others? These insights guide targeted changes to your routine.")
        ]
    },
    {
        "number": "07",
        "title": "Natural Supplements & Approaches",
        "content": [
            ("heading", "Evidence-Based Natural Approaches"),
            ("text", "While lifestyle changes form the foundation of blood sugar management, certain natural supplements and approaches have shown promise in scientific research. Always consult your healthcare provider before starting any supplement, especially if you take medications."),
            ("heading", "Supplements with Research Support"),
            ("table", {
                "headers": ["Supplement", "Potential Benefit", "Typical Dose"],
                "rows": [
                    ["Berberine", "May lower fasting glucose and A1C", "500mg 2-3x daily"],
                    ["Chromium", "May improve insulin sensitivity", "200-1000 mcg daily"],
                    ["Alpha-Lipoic Acid", "Antioxidant, may reduce insulin resistance", "300-600mg daily"],
                    ["Cinnamon", "May improve fasting glucose", "1-6g daily"],
                    ["Magnesium", "Supports insulin function", "200-400mg daily"],
                    ["Vitamin D", "Deficiency linked to insulin resistance", "1000-4000 IU daily"],
                ]
            }),
            ("heading", "Herbal Approaches"),
            ("text", "Several herbs have traditional use and emerging research for blood sugar support:"),
            ("bullets", [
                "Gymnema Sylvestre: Known as the 'sugar destroyer' in Ayurvedic medicine, may reduce sugar cravings",
                "Fenugreek: Seeds contain fiber that may slow carbohydrate digestion and absorption",
                "Bitter Melon: Contains compounds that may act like insulin",
                "American Ginseng: May improve post-meal blood sugar levels"
            ]),
            ("callout", "Important: Natural supplements are not a replacement for prescribed medications, a healthy diet, or regular exercise. They should be considered complementary approaches used alongside -- not instead of -- evidence-based medical care."),
            ("heading", "The Bliss Gums Approach"),
            ("text", "At Bliss Gums, we believe in supporting your wellness journey with carefully formulated products that complement a healthy lifestyle. Our approach focuses on quality ingredients backed by research, transparent labeling, and products designed to fit seamlessly into your daily routine."),
            ("text", "Visit blissgums.co to learn more about our product line and how we can support your blood sugar management goals.")
        ]
    },
    {
        "number": "08",
        "title": "Stress, Sleep & Blood Sugar",
        "content": [
            ("heading", "The Stress-Blood Sugar Connection"),
            ("text", "When you're stressed, your body releases hormones like cortisol and adrenaline. These hormones trigger your liver to release stored glucose, raising your blood sugar levels. This 'fight or flight' response was useful for our ancestors facing physical threats, but chronic stress keeps blood sugar elevated without the physical activity needed to use it."),
            ("heading", "Effective Stress Management Techniques"),
            ("bullets", [
                "Deep breathing exercises: Practice 4-7-8 breathing (inhale 4 seconds, hold 7, exhale 8)",
                "Progressive muscle relaxation: Systematically tense and release muscle groups",
                "Meditation: Even 10 minutes daily can reduce cortisol levels",
                "Nature exposure: Spending time outdoors lowers stress hormones",
                "Social connection: Meaningful relationships buffer against stress",
                "Journaling: Writing about stressors can help process and reduce their impact"
            ]),
            ("heading", "Sleep and Blood Sugar"),
            ("text", "Poor sleep has a profound effect on blood sugar regulation. Research shows that even one night of poor sleep can increase insulin resistance by up to 25%. Chronic sleep deprivation is associated with higher A1C levels and increased risk of type 2 diabetes."),
            ("heading", "Sleep Hygiene for Better Blood Sugar"),
            ("table", {
                "headers": ["Strategy", "How It Helps"],
                "rows": [
                    ["Consistent sleep schedule", "Regulates circadian rhythm and hormone cycles"],
                    ["7-9 hours per night", "Allows full hormonal recovery"],
                    ["Cool, dark bedroom", "Promotes deeper, more restorative sleep"],
                    ["No screens 1 hour before bed", "Reduces blue light interference with melatonin"],
                    ["Avoid late-night eating", "Prevents overnight blood sugar elevation"],
                    ["Limit caffeine after noon", "Prevents sleep disruption"],
                ]
            }),
            ("callout", "Did You Know? Studies show that people who sleep less than 6 hours per night have a significantly higher risk of developing type 2 diabetes, even when other risk factors are controlled for."),
            ("heading", "Creating a Stress-Sleep-Sugar Balance"),
            ("text", "Stress, sleep, and blood sugar are interconnected in a cycle: poor sleep increases stress, stress raises blood sugar, and high blood sugar can disrupt sleep. Breaking this cycle requires addressing all three factors together. Start with the area you have the most control over and build from there.")
        ]
    },
    {
        "number": "09",
        "title": "Working with Your Doctor",
        "content": [
            ("heading", "Building Your Healthcare Team"),
            ("text", "Managing blood sugar effectively often requires a team approach. Your healthcare team may include:"),
            ("bullets", [
                "Primary Care Physician: Your main doctor who coordinates overall care",
                "Endocrinologist: A specialist in hormone-related conditions including diabetes",
                "Certified Diabetes Educator (CDE): Provides practical education and support",
                "Registered Dietitian: Helps create personalized meal plans",
                "Pharmacist: Advises on medications and potential interactions",
                "Mental Health Professional: Supports emotional well-being and stress management"
            ]),
            ("heading", "Preparing for Your Appointments"),
            ("text", "Make the most of your doctor visits by coming prepared:"),
            ("bullets", [
                "Bring your blood sugar log or meter/app data",
                "List all medications and supplements you take",
                "Write down questions in advance",
                "Note any symptoms or changes since your last visit",
                "Be honest about your diet, exercise, and medication adherence",
                "Ask about any tests or screenings that are due"
            ]),
            ("heading", "Key Questions to Ask Your Doctor"),
            ("table", {
                "headers": ["Topic", "Questions to Ask"],
                "rows": [
                    ["Targets", "What are my personal blood sugar targets?"],
                    ["Testing", "How often should I test and when?"],
                    ["Medications", "Are my current medications optimal?"],
                    ["Complications", "What screenings do I need and how often?"],
                    ["Lifestyle", "What specific changes would benefit me most?"],
                ]
            }),
            ("callout", "Remember: You are the most important member of your healthcare team. No one knows your body better than you do. Speak up, ask questions, and be an active participant in your care."),
            ("heading", "When to Seek Immediate Medical Attention"),
            ("text", "Contact your doctor or seek emergency care if you experience:"),
            ("bullets", [
                "Blood sugar consistently above 300 mg/dL",
                "Symptoms of diabetic ketoacidosis (nausea, vomiting, fruity breath, confusion)",
                "Severe hypoglycemia (blood sugar below 54 mg/dL, loss of consciousness)",
                "Signs of infection that won't heal",
                "Sudden vision changes",
                "Chest pain or difficulty breathing"
            ])
        ]
    },
    {
        "number": "10",
        "title": "Frequently Asked Questions",
        "content": [
            ("heading", "Common Questions About Blood Sugar"),
            ("qa", "Can type 2 diabetes be reversed?", "While 'reversal' is debated among medical professionals, many people with type 2 diabetes have achieved normal blood sugar levels through significant lifestyle changes including weight loss, dietary improvements, and regular exercise. Some may be able to discontinue medications under medical supervision. However, the underlying predisposition may remain, requiring ongoing lifestyle management."),
            ("qa", "How quickly can lifestyle changes affect blood sugar?", "Many people see improvements in blood sugar levels within days to weeks of making dietary changes and increasing physical activity. Fasting blood sugar may improve within 1-2 weeks, while A1C changes take 2-3 months to fully reflect. Consistency is key for long-term results."),
            ("qa", "Is fruit bad for blood sugar?", "Most fruits are actually beneficial when eaten in appropriate portions. Berries, apples, pears, and citrus fruits are particularly good choices due to their lower glycemic index and high fiber content. The fiber in whole fruit slows sugar absorption compared to fruit juice. Aim for 2-3 servings per day."),
            ("qa", "Does stress really affect blood sugar?", "Absolutely. Stress hormones like cortisol and adrenaline directly raise blood sugar by triggering glucose release from the liver. Chronic stress can contribute to sustained elevated blood sugar levels and insulin resistance. Stress management is a legitimate and important part of blood sugar control."),
            ("qa", "How important is sleep for blood sugar?", "Very important. Research consistently shows that poor sleep quality and insufficient sleep duration are associated with higher blood sugar levels, increased insulin resistance, and greater risk of type 2 diabetes. Aim for 7-9 hours of quality sleep per night."),
            ("qa", "Can I eat sugar at all?", "Having diabetes or prediabetes doesn't mean you can never eat sugar again. The key is moderation, portion control, and being mindful of total carbohydrate intake. It's better to have a small amount of sugar as part of a balanced meal than to eat sugary foods on an empty stomach."),
            ("qa", "What about artificial sweeteners?", "Artificial sweeteners don't directly raise blood sugar, but research on their long-term effects is mixed. Some studies suggest they may affect gut bacteria or increase sugar cravings. If you use them, do so in moderation. Stevia and monk fruit are generally considered better options."),
            ("qa", "How often should I get my A1C checked?", "If your blood sugar is well-controlled, twice a year is typically sufficient. If you're adjusting treatment or not meeting targets, your doctor may recommend testing every 3 months. The A1C reflects your average blood sugar over the previous 2-3 months.")
        ]
    },
    {
        "number": "11",
        "title": "30-Day Action Plan",
        "content": [
            ("heading", "Your Step-by-Step Path to Better Blood Sugar"),
            ("text", "Change doesn't happen overnight. This 30-day plan breaks down the journey into manageable weekly goals, helping you build sustainable habits one step at a time."),
            ("heading", "Week 1: Foundation (Days 1-7)"),
            ("bullets", [
                "Day 1: Schedule a doctor appointment for baseline blood work",
                "Day 2: Start a food journal -- write down everything you eat and drink",
                "Day 3: Take a 10-minute walk after dinner",
                "Day 4: Clear your pantry of sugary drinks and processed snacks",
                "Day 5: Stock up on blood sugar-friendly foods (vegetables, lean proteins, whole grains)",
                "Day 6: Practice the plate method for all meals today",
                "Day 7: Review your food journal and identify your biggest sugar sources"
            ]),
            ("heading", "Week 2: Building Habits (Days 8-14)"),
            ("bullets", [
                "Day 8: Increase your post-meal walks to 15 minutes",
                "Day 9: Try a new low-glycemic recipe",
                "Day 10: Begin a simple stress management practice (5 minutes of deep breathing)",
                "Day 11: Set a consistent bedtime and wake time",
                "Day 12: Meal prep for the week ahead",
                "Day 13: Add a second daily walk (morning or lunch)",
                "Day 14: Review your progress -- celebrate your wins!"
            ]),
            ("heading", "Week 3: Deepening (Days 15-21)"),
            ("bullets", [
                "Day 15: Add resistance exercises (bodyweight squats, push-ups, resistance bands)",
                "Day 16: Experiment with apple cider vinegar before a meal",
                "Day 17: Try a 10-minute meditation session",
                "Day 18: Reduce portion sizes of starchy foods by 25%",
                "Day 19: Increase vegetable intake -- aim for vegetables at every meal",
                "Day 20: Try intermittent fasting (12-hour overnight fast)",
                "Day 21: Review your blood sugar log for patterns and trends"
            ]),
            ("heading", "Week 4: Optimizing (Days 22-30)"),
            ("bullets", [
                "Day 22: Increase exercise to 30 minutes per session",
                "Day 23: Research and discuss supplement options with your doctor",
                "Day 24: Create a go-to list of 10 blood sugar-friendly meals",
                "Day 25: Practice saying no to blood sugar-spiking treats",
                "Day 26: Connect with a support community or accountability partner",
                "Day 27: Schedule your follow-up blood work",
                "Day 28: Set specific 90-day goals for blood sugar, exercise, and nutrition",
                "Day 29: Plan your meals and exercise for the next month",
                "Day 30: Reflect on your journey -- you've built a strong foundation!"
            ]),
            ("callout", "Congratulations on completing the 30-day plan! Remember, this is just the beginning. The habits you've built this month are the foundation for long-term blood sugar health. Keep going, stay consistent, and don't hesitate to reach out to your healthcare team for support.")
        ]
    },
    {
        "number": "12",
        "title": "About Bliss Gums",
        "content": [
            ("heading", "Our Mission"),
            ("text", "At Bliss Gums, our mission is to make wellness simple, enjoyable, and accessible. We believe that managing your health shouldn't feel like a chore -- it should feel like a natural part of your daily routine."),
            ("heading", "Who We Are"),
            ("text", "Bliss Gums LLC is a wellness company based in Wyoming, United States. We specialize in developing innovative, great-tasting gummy supplements formulated with quality ingredients backed by science. Our products are designed to support your health goals while fitting seamlessly into your busy lifestyle."),
            ("heading", "Our Approach"),
            ("text", "We take a holistic approach to wellness that goes beyond just selling supplements. Through educational resources like this guide, we aim to empower our customers with the knowledge they need to make informed health decisions. We believe that true wellness comes from a combination of good nutrition, regular exercise, quality sleep, stress management, and targeted supplementation."),
            ("heading", "Quality Commitment"),
            ("bullets", [
                "All products manufactured in GMP-certified facilities",
                "Third-party tested for purity and potency",
                "Transparent labeling with no hidden ingredients",
                "Formulated based on current scientific research",
                "Made in the USA with globally sourced premium ingredients"
            ]),
            ("heading", "Connect With Us"),
            ("contact_table", {
                "rows": [
                    ["Website", "blissgums.co"],
                    ["Email", "info@blissgums.co"],
                    ["Location", "Wyoming, United States"],
                ]
            }),
            ("text", "We'd love to hear from you! Whether you have questions about our products, feedback on this guide, or just want to share your wellness journey, don't hesitate to reach out."),
            ("heading", "Thank You"),
            ("text", "Thank you for downloading The Complete Guide to Managing High Blood Sugar. We hope this resource helps you on your path to better health. Remember, every small step counts, and you don't have to do it alone."),
            ("text", "Here's to your health and happiness!"),
            ("text", "-- The Bliss Gums Team"),
            ("disclaimer", "Disclaimer: This guide is for informational purposes only and is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. The statements in this guide have not been evaluated by the Food and Drug Administration. Bliss Gums products are not intended to diagnose, treat, cure, or prevent any disease.")
        ]
    },
]


def draw_header_bar(c, page_width, page_height):
    """Draw green header bar with BLISS GUMS text."""
    bar_height = 32
    c.setFillColor(PRIMARY_COLOR)
    c.rect(0, page_height - bar_height, page_width, bar_height, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(MARGIN, page_height - 22, BRAND_NAME)


def draw_footer(c, page_width, page_height, page_num):
    """Draw footer with website and page number."""
    y = 30
    c.setFillColor(MEDIUM_GRAY)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN, y, WEBSITE)
    c.drawCentredString(page_width / 2, y, str(page_num))


class EbookDocTemplate(BaseDocTemplate):
    """Custom doc template that draws header/footer on each page."""

    def __init__(self, filename, **kwargs):
        self.page_count = 0
        self.skip_header_pages = {0, 1}  # Cover and TOC
        BaseDocTemplate.__init__(self, filename, **kwargs)

    def afterPage(self):
        self.page_count += 1


def build_cover_page(story, styles):
    """Build the cover page."""
    # We'll use a custom canvas approach for the cover
    story.append(Spacer(1, 0.1 * inch))

    # Top brand bar is drawn by canvas
    # Title section
    story.append(Spacer(1, 1.2 * inch))

    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=28,
        leading=34,
        alignment=TA_CENTER,
        textColor=DARK_TEXT,
    )
    story.append(Paragraph("The Complete Guide to<br/>Managing High Blood Sugar", title_style))
    story.append(Spacer(1, 0.3 * inch))

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=14,
        leading=18,
        alignment=TA_CENTER,
        textColor=MEDIUM_GRAY,
    )
    story.append(Paragraph("Diet &bull; Exercise &bull; Monitoring &bull; Wellness", subtitle_style))
    story.append(Spacer(1, 0.6 * inch))

    # Three feature boxes
    box_data = [["Blood Sugar", "12 Chapters", "2026 Edition"]]
    box_table = Table(box_data, colWidths=[2.2 * inch, 2.2 * inch, 2.2 * inch])
    box_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 0), (-1, -1), PRIMARY_COLOR),
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_GREEN_BG),
        ('BOX', (0, 0), (0, 0), 1, PRIMARY_COLOR),
        ('BOX', (1, 0), (1, 0), 1, PRIMARY_COLOR),
        ('BOX', (2, 0), (2, 0), 1, PRIMARY_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(box_table)

    story.append(Spacer(1, 3.0 * inch))

    # Footer info (above the bar)
    footer_style = ParagraphStyle(
        'CoverFooter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        alignment=TA_CENTER,
        textColor=white,
    )

    # Footer bar as table
    footer_data = [[f"{WEBSITE}  \u2022  {EMAIL}  \u2022  {LOCATION}"]]
    footer_table = Table(footer_data, colWidths=[PAGE_WIDTH - 2 * MARGIN])
    footer_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TEXTCOLOR', (0, 0), (-1, -1), white),
        ('BACKGROUND', (0, 0), (-1, -1), PRIMARY_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(footer_table)

    story.append(PageBreak())


def build_toc_page(story, styles):
    """Build the Table of Contents page."""
    story.append(Spacer(1, 0.6 * inch))

    label_style = ParagraphStyle(
        'TOCLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        textColor=PRIMARY_COLOR,
        spaceAfter=4,
    )
    story.append(Paragraph("TABLE OF CONTENTS", label_style))

    heading_style = ParagraphStyle(
        'TOCHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=DARK_TEXT,
        spaceAfter=6,
    )
    story.append(Paragraph("What's Inside", heading_style))

    # Green divider
    divider_data = [[""]]
    divider_table = Table(divider_data, colWidths=[PAGE_WIDTH - 2 * MARGIN], rowHeights=[3])
    divider_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), PRIMARY_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(divider_table)
    story.append(Spacer(1, 0.3 * inch))

    # Chapter list
    toc_entries = []
    for ch in CHAPTERS:
        toc_entries.append([ch["number"], ch["title"]])

    toc_table = Table(toc_entries, colWidths=[0.6 * inch, 5.4 * inch])
    toc_styles = [
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('TEXTCOLOR', (0, 0), (0, -1), PRIMARY_COLOR),
        ('TEXTCOLOR', (1, 0), (1, -1), DARK_TEXT),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LINEBELOW', (0, 0), (-1, -2), 0.5, LIGHT_GRAY),
    ]
    toc_table.setStyle(TableStyle(toc_styles))
    story.append(toc_table)

    story.append(PageBreak())


def build_chapter_page(story, styles, chapter):
    """Build a chapter page."""
    story.append(Spacer(1, 0.6 * inch))

    # Chapter label
    ch_label_style = ParagraphStyle(
        'ChapterLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        textColor=PRIMARY_COLOR,
        spaceAfter=4,
    )
    story.append(Paragraph(f"CHAPTER {chapter['number']}", ch_label_style))

    # Chapter title
    ch_title_style = ParagraphStyle(
        'ChapterTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=DARK_TEXT,
        spaceAfter=6,
    )
    story.append(Paragraph(chapter['title'], ch_title_style))

    # Green divider
    divider_data = [[""]]
    divider_table = Table(divider_data, colWidths=[PAGE_WIDTH - 2 * MARGIN], rowHeights=[3])
    divider_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), PRIMARY_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(divider_table)
    story.append(Spacer(1, 0.2 * inch))

    # Body styles
    body_style = ParagraphStyle(
        'ChapterBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=15,
        alignment=TA_JUSTIFY,
        textColor=DARK_TEXT,
        spaceAfter=8,
    )

    subheading_style = ParagraphStyle(
        'ChapterSubheading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=DARK_TEXT,
        spaceBefore=12,
        spaceAfter=6,
    )

    bullet_style = ParagraphStyle(
        'ChapterBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=DARK_TEXT,
        leftIndent=20,
        spaceAfter=3,
        bulletIndent=8,
    )

    # Process content
    for item in chapter['content']:
        item_type = item[0]

        if item_type == "heading":
            story.append(Paragraph(item[1], subheading_style))

        elif item_type == "text":
            story.append(Paragraph(item[1], body_style))

        elif item_type == "bullets":
            for bullet in item[1]:
                story.append(Paragraph(f"\u2022  {bullet}", bullet_style))
            story.append(Spacer(1, 4))

        elif item_type == "callout":
            callout_text = item[1]
            callout_style = ParagraphStyle(
                'Callout',
                parent=styles['Normal'],
                fontName='Helvetica',
                fontSize=10,
                leading=14,
                textColor=DARK_TEXT,
                alignment=TA_JUSTIFY,
            )
            callout_data = [[Paragraph(callout_text, callout_style)]]
            callout_table = Table(callout_data, colWidths=[PAGE_WIDTH - 2 * MARGIN - 16])
            callout_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), LIGHT_GREEN_BG),
                ('BOX', (0, 0), (-1, -1), 1.5, PRIMARY_COLOR),
                ('TOPPADDING', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
                ('LEFTPADDING', (0, 0), (-1, -1), 12),
                ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ]))
            story.append(Spacer(1, 6))
            story.append(callout_table)
            story.append(Spacer(1, 6))

        elif item_type == "table":
            table_info = item[1]
            headers = table_info["headers"]
            rows = table_info["rows"]
            all_data = [headers] + rows

            num_cols = len(headers)
            col_width = (PAGE_WIDTH - 2 * MARGIN) / num_cols
            col_widths = [col_width] * num_cols

            t = Table(all_data, colWidths=col_widths)
            table_styles = [
                ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_COLOR),
                ('TEXTCOLOR', (0, 0), (-1, 0), white),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 9),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 9),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#d1d5db")),
                ('TOPPADDING', (0, 0), (-1, -1), 6),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                ('LEFTPADDING', (0, 0), (-1, -1), 8),
                ('RIGHTPADDING', (0, 0), (-1, -1), 8),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
            ]
            t.setStyle(TableStyle(table_styles))
            story.append(Spacer(1, 6))
            story.append(t)
            story.append(Spacer(1, 6))

        elif item_type == "qa":
            question = item[1]
            answer = item[2]
            q_style = ParagraphStyle(
                'Question',
                parent=styles['Normal'],
                fontName='Helvetica-Bold',
                fontSize=11,
                leading=14,
                textColor=PRIMARY_COLOR,
                spaceBefore=10,
                spaceAfter=4,
            )
            story.append(Paragraph(f"Q: {question}", q_style))
            story.append(Paragraph(answer, body_style))

        elif item_type == "contact_table":
            table_info = item[1]
            rows = table_info["rows"]

            t = Table(rows, colWidths=[1.5 * inch, 4.0 * inch])
            t.setStyle(TableStyle([
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('TEXTCOLOR', (0, 0), (0, -1), PRIMARY_COLOR),
                ('TEXTCOLOR', (1, 0), (1, -1), DARK_TEXT),
                ('TOPPADDING', (0, 0), (-1, -1), 6),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                ('LINEBELOW', (0, 0), (-1, -2), 0.5, LIGHT_GRAY),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]))
            story.append(Spacer(1, 6))
            story.append(t)
            story.append(Spacer(1, 6))

        elif item_type == "disclaimer":
            disclaimer_style = ParagraphStyle(
                'Disclaimer',
                parent=styles['Normal'],
                fontName='Helvetica',
                fontSize=7.5,
                leading=10,
                textColor=MEDIUM_GRAY,
                alignment=TA_JUSTIFY,
                spaceBefore=20,
            )
            # Draw a light line above
            story.append(Spacer(1, 12))
            line_data = [[""]]
            line_table = Table(line_data, colWidths=[PAGE_WIDTH - 2 * MARGIN], rowHeights=[1])
            line_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), LIGHT_GRAY),
                ('TOPPADDING', (0, 0), (-1, -1), 0),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ]))
            story.append(line_table)
            story.append(Spacer(1, 6))
            story.append(Paragraph(item[1], disclaimer_style))

    story.append(PageBreak())


class CoverCanvas(canvas.Canvas):
    """Custom canvas that draws header bar on cover and TOC, and standard header/footer on other pages."""

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._page_number = 0
        self._saved_pages = []

    def showPage(self):
        self._saved_pages.append(dict(self.__dict__))
        self._page_number += 1
        canvas.Canvas.showPage(self)

    def save(self):
        num_pages = self._page_number
        for i in range(num_pages):
            page = self._saved_pages[i]
        canvas.Canvas.save(self)


def on_page_cover(canvas_obj, doc):
    """Draw cover page decorations."""
    canvas_obj.saveState()
    w, h = PAGE_WIDTH, PAGE_HEIGHT

    # Top green bar
    bar_h = 40
    canvas_obj.setFillColor(PRIMARY_COLOR)
    canvas_obj.rect(0, h - bar_h, w, bar_h, fill=1, stroke=0)
    canvas_obj.setFillColor(white)
    canvas_obj.setFont("Helvetica-Bold", 14)
    canvas_obj.drawCentredString(w / 2, h - 28, BRAND_NAME)

    canvas_obj.restoreState()


def on_page_toc(canvas_obj, doc):
    """Draw TOC page decorations."""
    canvas_obj.saveState()
    w, h = PAGE_WIDTH, PAGE_HEIGHT

    # Top green bar
    draw_header_bar(canvas_obj, w, h)
    # Footer
    draw_footer(canvas_obj, w, h, 2)

    canvas_obj.restoreState()


def on_page_chapter(canvas_obj, doc):
    """Draw chapter page decorations."""
    canvas_obj.saveState()
    w, h = PAGE_WIDTH, PAGE_HEIGHT

    # Top green bar
    draw_header_bar(canvas_obj, w, h)
    # Footer with page number
    page_num = doc.page
    draw_footer(canvas_obj, w, h, page_num)

    canvas_obj.restoreState()


def generate_pdf():
    """Generate the complete ebook PDF."""
    doc = BaseDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
        title="The Complete Guide to Managing High Blood Sugar - 2026 Edition",
        author="Bliss Gums LLC",
        subject="Blood Sugar Management Guide",
        creator="Bliss Gums",
    )

    # Define frames
    content_frame = Frame(
        MARGIN, MARGIN + 20,
        PAGE_WIDTH - 2 * MARGIN,
        PAGE_HEIGHT - 2 * MARGIN - 20,
        id='content'
    )

    cover_frame = Frame(
        MARGIN, MARGIN,
        PAGE_WIDTH - 2 * MARGIN,
        PAGE_HEIGHT - 2 * MARGIN,
        id='cover'
    )

    # Page templates
    cover_template = PageTemplate(id='cover', frames=[cover_frame], onPage=on_page_cover)
    toc_template = PageTemplate(id='toc', frames=[content_frame], onPage=on_page_toc)
    chapter_template = PageTemplate(id='chapter', frames=[content_frame], onPage=on_page_chapter)

    doc.addPageTemplates([cover_template, toc_template, chapter_template])

    styles = getSampleStyleSheet()
    story = []

    # ── Cover Page ──
    build_cover_page(story, styles)

    # Switch to TOC template
    from reportlab.platypus.doctemplate import NextPageTemplate
    story.insert(-1, NextPageTemplate('toc'))

    # ── TOC Page ──
    build_toc_page(story, styles)

    # Switch to chapter template
    story.insert(-1, NextPageTemplate('chapter'))

    # ── Chapter Pages ──
    for chapter in CHAPTERS:
        build_chapter_page(story, styles, chapter)

    # Build the document
    doc.build(story)
    print(f"PDF generated successfully: {OUTPUT_PATH}")

    # Copy to digital-marketing-playbook.pdf
    shutil.copy2(OUTPUT_PATH, COPY_PATH)
    print(f"PDF copied to: {COPY_PATH}")


if __name__ == "__main__":
    generate_pdf()
