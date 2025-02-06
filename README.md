# 🚀 Projectile Motion Simulator  

A **Python-based simulation** that models **projectile motion** with and without **air resistance**. The program calculates the **trajectory, flight time, range, and maximum height** of a projectile and plots the motion graphically.  

## 🔥 Features  
✅ Simulates projectile motion **with and without air resistance**  
✅ Plots **trajectories for comparison**  
✅ Uses **numerical integration (Euler's method)** for realistic motion under drag  
✅ Customizable **drag coefficient (Cd), mass, and cross-sectional area**  

---

## 📌 How It Works  
1. The user enters **initial velocity** and **launch angle**.  
2. The program asks if they want to include **air resistance**.  
3. If **yes**, the user inputs:  
   - **Drag coefficient (Cd)** (default ~0.47 for a sphere)  
   - **Mass of the projectile** (kg)  
   - **Cross-sectional area (m²)**  
4. The simulation calculates the projectile’s motion:  
   - **Without air resistance** (using kinematic equations).  
   - **With air resistance** (using Euler’s method for numerical integration).  
5. The program **plots both trajectories** and **displays key results**.  

---

## 🎯 Example Output  
### **Graph Example**  
When run, the program will generate a graph comparing **ideal motion** vs. **motion under drag**:  

![image](https://github.com/user-attachments/assets/6b018bc9-2144-4c4f-b985-2ea705c92f64)

*Note: This is a placeholder image. The actual graph is generated in Python.*  

### **Console Output Example**  
1. Enter initial velocity (m/s): 50
2. Enter launch angle (degrees): 45
3. Include air resistance? (yes/no): yes
4. Enter drag coefficient (Cd) (default ~0.47 for a sphere): 0.47
5. Enter object mass (kg): 1
6. Enter cross-sectional area (m²): 0.01

- Time of Flight (No Air Resistance): 7.14 seconds
- Range (With Air Resistance): 85.30 meters
- Range (No Air Resistance): 255.08 meters

---

## 🛠 Installation & Usage  
### **1️⃣ Install Dependencies**  
Ensure you have **Python** installed. Then, install required libraries:  
```bash
pip install numpy matplotlib
```

---

##2️⃣ Run the Program
```bash
python motion.py
```


