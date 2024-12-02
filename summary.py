import openai
import csv
import os

client = openai.OpenAI(
    api_key="sk-whnUEfTKRKbE8-73nOgpcg",
    base_url="https://cmu.litellm.ai",
)

def summarize_text(text):
    try:
        # Generate summary using OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o",  # Adjust model based on needs
            messages=[{"role": "user", "content": f"Using the record of the conversation, write a summary of what the interactions about. If they forgot something, make note of that. :\n\n{text}"}],
            max_tokens=50,  # Adjust max tokens for brevity of summary
            temperature=0.5
        )
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        print(f"Error generating summary: {e}")
        return None

def summarize_csv(input_csv, output_csv):
    with open(input_csv, mode='r') as infile, open(output_csv, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        headers = next(reader)  # Assuming first row is the header
        writer.writerow(headers + ["Summary"])  # Add "Summary" column to headers

        for row in reader:
            # Combine relevant columns (adjust based on your CSV structure)
            text_to_summarize = " ".join(row)
            summary = summarize_text(text_to_summarize)
            writer.writerow(row + [summary])  # Append summary to each row

# Example usage
input_csv = "/Users/raynahata/Desktop/Github/TTRProject/conversation_history.csv"
output_csv = "/Users/raynahata/Desktop/Github/TTRProject/summary_csv.csv"
summarize_csv(input_csv, output_csv)