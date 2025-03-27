# **VOZNSENSKYLAB:POETICS**

**VOZNESENSKYLAB:POETICS** – проект, посвященный созданию нелинейного электронного издания стихотворений А. А. Вознесенского. В издании (будут) реализованы читательские сценарии: деление по метру, сложности текстов, темам, случайные и др. Читательский сценарий делит корпус стихотворений, вошедших в издание, на категории, релизует навигацую внутри и между этими категориями и позволяет читателю погружаться в творчество Вознесенского, опираясь на собственные представления и опыт.

На данный момент содержательно реализованы сценарии: тема, метр, сложность, хронология.

## **Структура проекта**:  
### **1. Корпуса А. А. Вознесенского (папка corpora)**
   В рамках работы над проектами нами использовались и разрабатывались сразу несколько корпусов А. А. Вознесенского:
   #### **Вычитанный и пока неполный корпус в папке `vozn_complete_processed`**  
   В этой папке хранится вычитанный и исправленный корпус с текстовыми стихотворениями Вознесенского, который планируется дополнить до полного собрания. На данный момент в корпусе около 600 произведений вычитанных вручную. Корпус не собран до конца, по примерным подсчетам в полный корпус должно входить ~1500 стихотворных произведений. В папке `vozn_editions` хранится таблица со списком изданий, откуда взяты данные для этого корпуса. 
   
   В корпус входит таблица с информацией о стихотворениях `vozn_corpus_processed(in progress).xlsx`. Другая часть корпуса - это папка, где хранятся вычитанные и размеченные тексты стихотворений `vozn_complete_poems`.  
   Стихотворения размечаются тегами (разметка позаимствована у Б. В. Орехова):

      `<n>` - название;  
      `<rm>`- любая нестихотворная строка (чаще всего посвящения);  
      `<&>` - первая строка стихотворения;  
      `<#>` - дата.

   #### **Семлированный корпус А.А.Вознесенского в папке `vozn_sample`**
   Семплированный корпус А. А. Вознесенского включает в себя по 60-70 стихотворений каждого десятилетия (кроме 1940-х) периода творческой активности А.А. Вознесенского: от 1950-х до 2000-х. Структурно аналогичен корпусу `vozn_complete_processed` и является более ранней и сбалансированной его версией. Использован для разработки сценариев, основанных на метриках удобочитаемости и автоматической разметке стихотворного метра.

   #### **Полный и невычитанный корпус А. А. Вознесенского**
   В корпус входят произведения, вошедшие в полное собрание сочинений А. А. Вознесенского издательства "Альфа-книга". Таблица `vozn_complete_raw.xlsx` с стихотворениями и информацией о них хранится в папке `vozn_complete_raw`.

### **2. Реализация читательских сценариев (папка `scenarios`)**
В папке хранятся результаты автоматического анализа творчества А.А.Вознесенского. Каждому сценарию соответствует свой этап анализа и своя папка. В папках хранится код, с помощью которого был произведен анализ, данные, которые анализировались и результаты анализа в отдельных xlsx-таблицах. Методология подробно исследования описана в файле `Paper VOZNESENSKYLAB_POETICS.docx`.

#### Читательские сценарии и их папки:

* **Сценарий "сложность" (папка complexity)**  
   Удобочитаемость оценивалась формулами Мацковского и формулами Оборневой, лексическое разнообразие оценивалось формулой TTR (type-token ratio).
* **Сценарий "метр" (папка metre)**  
   Разметка ударений производилась с помощью библиотеки `ru_accent_poet`, а код для разметки метра хранится в этой папке.
* **Сценарий "тема" (папка theme)**  
  Тематическое моделирование произвоидлось с помощью NMF-модели.  

### **3. Отчетные материалы (папка slides)**

Этапы работы над проектом описаны в презентациях, которые хранятся в папке `slides`. 
