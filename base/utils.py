# To_Do_list_CSE370/utils.py
class StudyTimer:
    @staticmethod
    def get_timer_js(duration):
        return f'''
        document.addEventListener('DOMContentLoaded', function () {{
            const timerDisplay = document.getElementById('timer');
            let timeLeft = {duration};

            function updateTimerDisplay() {{
                const minutes = Math.floor(timeLeft / 60);
                const seconds = timeLeft % 60;
                timerDisplay.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
            }}

            function startTimer() {{
                updateTimerDisplay();
                const timerInterval = setInterval(function () {{
                    if (timeLeft <= 0) {{
                        clearInterval(timerInterval);
                        timerDisplay.textContent = "00:00";
                        // Additional logic when the timer reaches 0
                    }} else {{
                        timeLeft--;
                        updateTimerDisplay();
                    }}
                }}, 1000);
            }}

            startTimer();
        }});
        '''
