class PassAndInterceptionDetector():
    def __init__(self):
        pass 

    def detect_passes(self,ball_acquisition,player_assignment):
        """
        Detects ball passes in the sequence of frames.
        
        :return: List indicating the team that made the pass at each frame (-1 if no pass).
        """
        passes = [-1] * len(ball_acquisition)
        prev_holder=-1
        previous_frame=-1

        for frame in range(1, len(ball_acquisition)):
            if ball_acquisition[frame - 1] != -1:
                prev_holder = ball_acquisition[frame - 1]
                previous_frame= frame - 1
            
            current_holder = ball_acquisition[frame]
            
            if prev_holder != -1 and current_holder != -1 and prev_holder != current_holder:
                prev_team = player_assignment[previous_frame].get(prev_holder, -1)
                current_team = player_assignment[frame].get(current_holder, -1)

                if prev_team == current_team and prev_team != -1:
                    passes[frame] = prev_team

        return passes

    def detect_interceptions(self,ball_acquisition,player_assignment):
        """
        Detects ball interceptions in the sequence of frames.
        
        :return: List indicating the team that made the interception at each frame (-1 if no interception).
        """
        interceptions = [-1] * len(ball_acquisition)
        
        for frame in range(1, len(ball_acquisition)):
            prev_holder = ball_acquisition[frame - 1]
            current_holder = ball_acquisition[frame]
            
            if prev_holder != -1 and current_holder != -1 and prev_holder != current_holder:
                prev_team = player_assignment[frame - 1].get(prev_holder, -1)
                current_team = player_assignment[frame].get(current_holder, -1)
                
                if prev_team != current_team and prev_team != -1 and current_team != -1:
                    interceptions[frame] = current_team
        
        return interceptions