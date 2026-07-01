# 如何使用Record

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-98

构造一个对象类型，其属性键为“Keys” ，其属性值为“Type”，可用于将一种类型的属性映射到另一种类型。
 
示例如下：
 
```text
<em>// Define course types</em>
type Course = 'Math' | 'Chinese' | 'English';

<em>// Define grade types</em>
type Grade = number;

<em>// Define student grade record types</em>
type StudentGrades = Record<Course, Grade>;

<em>// Define the type of class grade record, where the key is the student ID and the value is the student's grade record</em>
type ClassGrades = Record<string, StudentGrades>;

interface StudentCourseGrade {
  Math: number,
  Chinese: number,
  English: number
}

let student1: StudentCourseGrade = {
  Math: 90,
  Chinese: 85,
  English: 92
}
let student2: StudentCourseGrade = {
  Math: 78,
  Chinese: 82,
  English: 85
}
let student3: StudentCourseGrade = {
  Math: 95,
  Chinese: 89,
  English: 90
}

<em>// Initialize class grades</em>
const classGrades: ClassGrades = {
  '001': student1,
  '002': student2,
  '003': student3
};

@Entry
@Component
struct Index {
 <em> // Obtain the average grade of a student</em>
  getAverageGrade(studentId: string, grades: ClassGrades): number | null {
    const studentGrades = grades[studentId]; <em>// Obtain corresponding grade data for students</em>
    if (!studentGrades) {
      console.log(`Student with ID ${studentId} not found.`);
      return null;
    }

    const courses = Object.keys(studentGrades) as Course[]; <em>// Course type array</em>
   <em> // Calculate the total grade of the course</em>
    const total = courses.reduce((sum, course) => sum + studentGrades[course], 0);
    return total / courses.length; <em>// Average score</em>
  }

  build() {
    Row() {
      Column() {
        Button('getAverageGrade')
          .onClick(() => {
           <em> // output: 89</em>
            console.log('student average grade is:', this.getAverageGrade('001', classGrades));
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
